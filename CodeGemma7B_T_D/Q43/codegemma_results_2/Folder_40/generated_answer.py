def find_primes_between_indices(integers):
    primes = []
    for i in range(1, len(integers) + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return sorted(primes)