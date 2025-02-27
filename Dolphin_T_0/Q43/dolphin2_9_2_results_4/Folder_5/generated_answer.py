def find_primes_between_indices(lst):
    primes = []
    for i, n in enumerate(lst[27:87], 28):
        if all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))):
            primes.append(n)
    return sorted(primes, reverse=True)