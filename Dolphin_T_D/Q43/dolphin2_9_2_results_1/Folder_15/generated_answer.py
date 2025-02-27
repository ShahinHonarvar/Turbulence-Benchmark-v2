def find_primes_between_indices(lst):
    primes = [i for i in lst[5:] if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    if primes:
        return sorted(primes, reverse=True)
    else:
        return []