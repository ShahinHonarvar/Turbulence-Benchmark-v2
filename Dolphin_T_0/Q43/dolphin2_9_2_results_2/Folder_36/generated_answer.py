def find_primes_between_indices(lst):
    primes = [n for n in lst[229:851] if all((n % i != 0 for i in range(2, n)))]
    return sorted(primes, reverse=True)