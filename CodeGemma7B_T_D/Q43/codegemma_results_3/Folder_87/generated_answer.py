def find_primes_between_indices(lst):
    primes = []
    for i in range(11, 42):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    primes.sort(reverse=True)
    return primes if primes else []