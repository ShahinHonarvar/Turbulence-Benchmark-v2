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

    def factors(n):
        factor_set = set()
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                if is_prime(i):
                    factor_set.add(i)
                n //= i
        if n > 1 and is_prime(n):
            factor_set.add(n)
        return factor_set
    if len(lst) <= 6:
        return set()
    return factors(lst[6])