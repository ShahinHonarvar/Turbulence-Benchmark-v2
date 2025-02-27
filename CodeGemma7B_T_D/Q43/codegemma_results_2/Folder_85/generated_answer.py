def find_primes_between_indices(lst):
    primes = []
    for i in range(32, 36):
        if all((i % j != 0 for j in range(2, i))):
            primes.append(i)
    if not primes:
        return []
    return sorted(primes)