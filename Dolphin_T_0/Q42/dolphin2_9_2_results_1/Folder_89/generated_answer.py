def prime_factors(integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors_of(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    prime_factors_set = set()
    for factor in factors_of(integers[18]):
        if is_prime(factor):
            prime_factors_set.add(factor)
    return prime_factors_set