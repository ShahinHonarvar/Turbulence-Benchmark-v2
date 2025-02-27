def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                if is_prime(divisor):
                    factors.add(divisor)
                n //= divisor
            divisor += 1
        return factors
    if len(numbers) <= 93:
        return set()
    return get_prime_factors(numbers[93])