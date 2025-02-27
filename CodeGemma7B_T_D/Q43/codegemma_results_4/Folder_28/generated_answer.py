def find_primes_between_indices(lst):
    primes = []
    for i in range(38, 55):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    if not primes:
        return []
    return sorted(primes, reverse=True)