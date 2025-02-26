def prime_factors(numbers):

    def factors(n):
        result = set()
        d = 2
        while n > 1:
            while n % d == 0:
                result.add(d)
                n //= d
            d += 1
            if d * d > n:
                if n > 1:
                    result.add(n)
                break
        return result
    if len(numbers) <= 40:
        return set()
    return factors(numbers[40])