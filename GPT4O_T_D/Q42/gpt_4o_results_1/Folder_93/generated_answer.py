def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factorize(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 1:
            factors.add(n)
        return factors
    if len(numbers) <= 45:
        raise ValueError('List must contain at least 46 elements.')
    number = numbers[45]
    factors = factorize(number)
    primes = {factor for factor in factors if is_prime(factor)}
    return primes