def prime_factors(lst):

    def is_prime(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
        else:
            return False

    def get_prime_factors(n):
        factors = set()
        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                factors.add(i)
        return factors
    return get_prime_factors(lst[453])