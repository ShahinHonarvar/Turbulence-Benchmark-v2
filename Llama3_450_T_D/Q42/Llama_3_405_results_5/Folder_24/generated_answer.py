def prime_factors(numbers):

    def get_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if len(numbers) > 74:
        return get_prime_factors(numbers[74])
    else:
        return set()