def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors_set = set()
        for i in range(2, n + 1):
            while n % i == 0:
                if is_prime(i):
                    factors_set.add(i)
                n //= i
        return factors_set
    if len(lst) > 126:
        return factors(lst[126])
    else:
        return set()