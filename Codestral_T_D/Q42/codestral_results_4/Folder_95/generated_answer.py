def prime_factors(num_list):

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

    def get_factors(n):
        factors = set()
        d = 2
        while d * d <= n:
            if n % d == 0:
                if is_prime(d):
                    factors.add(d)
                n //= d
            else:
                d += 1
        if n > 1 and is_prime(n):
            factors.add(n)
        return factors
    return get_factors(num_list[87])