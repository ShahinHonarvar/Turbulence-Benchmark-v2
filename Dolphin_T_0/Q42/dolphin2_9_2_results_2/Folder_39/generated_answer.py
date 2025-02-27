def prime_factors(num_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = []
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    n = num_list[59]
    prime_factors_set = set()
    for factor in get_factors(n):
        if is_prime(factor):
            prime_factors_set.add(factor)
    return prime_factors_set