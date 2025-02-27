def find_primes_between_indices(lst):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or (n > 2 and n % 3 == 0):
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    return sorted([n for n in lst[430:806] if is_prime(n)])