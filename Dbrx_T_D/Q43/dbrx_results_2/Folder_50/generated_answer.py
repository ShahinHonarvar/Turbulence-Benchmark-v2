def find_primes_between_indices(lst):
    primes = []
    for i in range(23, 60):
        if i < 0 or i >= len(lst):
            break
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(lst[i])
    if not primes:
        return primes
    else:
        return sorted(primes, reverse=True)