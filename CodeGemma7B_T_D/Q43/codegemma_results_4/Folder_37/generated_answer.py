from math import sqrt

def find_primes_between_indices(_, lst):
    return sorted([i for i in lst[13:69] if all((i % d != 0 for d in range(3, int(sqrt(i)) + 1, 2)))]) or []