def prime_factors(numbers):

    def get_prime_factors(n):
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
    if len(numbers) <= 68 or not isinstance(numbers[68], int) or numbers[68] <= 0:
        return set()
    return get_prime_factors(numbers[68])