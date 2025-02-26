def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            else:
                divisor += 1
        if n > 1:
            factors.add(n)
        return factors
    return get_prime_factors(numbers[100])