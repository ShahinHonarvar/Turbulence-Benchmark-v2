def prime_factors(int_list):

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
        if n <= 1:
            return set()
        factor_set = set()
        divisor = 2
        while n % divisor == 0 and is_prime(divisor):
            factor_set.add(divisor)
            n //= divisor
        divisor = 3
        while n % divisor == 0 and is_prime(divisor):
            factor_set.add(divisor)
            n //= divisor
        p = 5
        while p * p <= n:
            for divisor in (p, p + 2):
                while n % divisor == 0 and is_prime(divisor):
                    factor_set.add(divisor)
                    n //= divisor
            p += 6
        if n > 1 and is_prime(n):
            factor_set.add(n)
        return factor_set
    return factors(int_list[132])