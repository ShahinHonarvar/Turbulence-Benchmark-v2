def prime_factors(integers):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        return factors
    if len(integers) > 87:
        return get_prime_factors(integers[87])
    return set()