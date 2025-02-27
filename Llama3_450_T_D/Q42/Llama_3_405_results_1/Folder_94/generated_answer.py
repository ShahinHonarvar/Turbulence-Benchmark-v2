def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if len(numbers) <= 93:
        return set()
    return get_prime_factors(numbers[93])