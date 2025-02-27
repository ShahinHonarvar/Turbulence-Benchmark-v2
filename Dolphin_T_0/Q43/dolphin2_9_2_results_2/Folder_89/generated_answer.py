def find_primes_between_indices(lst):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    primes = [x for x in lst[69:85] if is_prime(x)]
    return sorted(primes, reverse=True) if primes else []