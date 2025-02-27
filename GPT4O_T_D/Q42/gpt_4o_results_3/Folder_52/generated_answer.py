def prime_factors(numbers):

    def get_factors(n):
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
    if len(numbers) > 478:
        return get_factors(numbers[478])
    else:
        return set()