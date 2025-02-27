def find_primes_between_indices(lst):
    primes = [x for x in lst[19:91] if all((x % y != 0 for y in range(2, int(x ** 0.5) + 1)))]
    primes.sort(reverse=True)
    return primes