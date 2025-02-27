def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((p for p in range(2, lst[990] + 1) if is_prime(p) and lst[990] % p == 0))