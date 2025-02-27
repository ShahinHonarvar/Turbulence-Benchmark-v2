def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        div = 2
        while div * div <= n:
            while n % div == 0:
                factors.add(div)
                n //= div
            div += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(numbers) <= 74:
        return set()
    return get_prime_factors(numbers[74])