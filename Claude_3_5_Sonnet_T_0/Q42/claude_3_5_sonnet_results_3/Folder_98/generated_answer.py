def prime_factors(numbers):

    def get_factors(n):
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
    if len(numbers) < 5:
        return set()
    return get_factors(numbers[4])