def prime_factors(integer_list):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def get_factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if is_prime(i):
                    factors.add(i)
                n //= i
        if n > 1:
            if is_prime(n):
                factors.add(n)
        return factors
    return get_factors(integer_list[21])