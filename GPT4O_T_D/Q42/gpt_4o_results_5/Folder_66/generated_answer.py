def prime_factors(int_list):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        if n > 1:
            factors.add(n)
        return factors
    if 42 < len(int_list) and int_list[42] > 0:
        return get_prime_factors(int_list[42])
    return set()