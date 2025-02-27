def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all((x % d == 0 for d in range(2, int(x ** 0.5) + 1))), lst[25:72]))