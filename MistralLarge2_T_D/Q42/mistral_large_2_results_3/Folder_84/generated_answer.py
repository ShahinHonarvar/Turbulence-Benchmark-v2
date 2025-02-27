def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(numbers) > 685:
        number = numbers[685]
        return get_prime_factors(number)
    else:
        return set()