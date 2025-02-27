def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = [n for n in lst[15:49] if is_prime(n)]
    return sorted(primes, reverse=True) if primes else []