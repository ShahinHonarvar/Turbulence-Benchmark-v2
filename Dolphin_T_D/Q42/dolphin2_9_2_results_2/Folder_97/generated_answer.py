def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        if n != 1:
            factors.add(n)
        return factors
    prime_set = set()
    if is_prime(lst[132]):
        prime_set.add(lst[132])
    else:
        prime_factors_list = get_factors(lst[132])
        for factor in prime_factors_list:
            if is_prime(factor):
                prime_set.add(factor)
    return prime_set