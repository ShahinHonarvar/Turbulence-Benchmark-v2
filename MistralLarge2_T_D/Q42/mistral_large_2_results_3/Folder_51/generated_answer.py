def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_prime_factors(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0:
                if is_prime(i):
                    factors.add(i)
                n //= i
        return factors
    if len(lst) > 64:
        return get_prime_factors(lst[64])
    else:
        return set()