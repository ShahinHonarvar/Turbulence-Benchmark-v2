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
        factors_set = set()
        d = 2
        while d * d <= n:
            if n % d == 0:
                if is_prime(d):
                    factors_set.add(d)
                if is_prime(n // d):
                    factors_set.add(n // d)
            d += 1
        if is_prime(n):
            factors_set.add(n)
        return factors_set
    return factors(lst[27])