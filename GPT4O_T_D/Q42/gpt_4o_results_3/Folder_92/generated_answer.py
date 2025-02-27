def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    if not numbers:
        return set()
    return get_prime_factors(numbers[0])