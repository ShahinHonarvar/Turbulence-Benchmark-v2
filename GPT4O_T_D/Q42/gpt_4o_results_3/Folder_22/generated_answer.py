def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= 2:
            while n % divisor == 0:
                if is_prime(divisor):
                    factors.add(divisor)
                n //= divisor
            divisor += 1
        return factors
    if len(numbers) <= 72:
        return set()
    return get_prime_factors(numbers[72])