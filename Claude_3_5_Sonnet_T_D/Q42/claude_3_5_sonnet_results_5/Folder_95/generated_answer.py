def prime_factors(numbers):

    def factorize(n):
        factors = set()
        d = 2
        while n > 1:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1
            if d * d > n:
                if n > 1:
                    factors.add(n)
                break
        return factors
    if len(numbers) <= 87 or not isinstance(numbers[87], int) or numbers[87] <= 0:
        return set()
    return factorize(numbers[87])