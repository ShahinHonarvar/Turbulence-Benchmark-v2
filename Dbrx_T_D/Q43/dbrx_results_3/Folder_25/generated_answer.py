def find_primes_between_indices(lst):
    prime = [x for x in lst[52:54] if all((y % x != 0 for y in range(2, x)))]
    return sorted(prime)