def find_primes_between_indices(lst):

    def is_prime(n):
        if n in (0, 1):
            return False
        for factor in range(2, int(n ** 0.5) + 1):
            if n % factor == 0:
                return False
        return True
    return sorted([x for x in lst[33:36] if is_prime(x)])