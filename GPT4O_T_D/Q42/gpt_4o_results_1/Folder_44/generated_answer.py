def prime_factors(numbers):
    index = 828
    if index >= len(numbers):
        return set()

    def factorize(n):
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
    return factorize(numbers[index])