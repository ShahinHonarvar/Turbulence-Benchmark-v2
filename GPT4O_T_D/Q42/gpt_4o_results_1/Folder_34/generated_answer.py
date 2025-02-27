def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 2
        if n > 2:
            factors.add(n)
        return factors
    if len(numbers) > 97:
        return get_prime_factors(numbers[97])
    else:
        return set()