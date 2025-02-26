def prime_factors(numbers):

    def factors(n):
        f = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                f.add(d)
                n //= d
            d += 1
        if n > 1:
            f.add(n)
        return f
    return factors(numbers[53])