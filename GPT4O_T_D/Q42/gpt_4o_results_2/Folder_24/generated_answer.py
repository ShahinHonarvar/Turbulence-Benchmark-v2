def prime_factors(numbers):

    def get_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    return get_prime_factors(numbers[74]) if 74 < len(numbers) else set()