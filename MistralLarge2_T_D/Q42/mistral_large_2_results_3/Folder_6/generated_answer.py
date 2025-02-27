def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= 2:
            if n % divisor == 0:
                if is_prime(divisor):
                    factors.add(divisor)
                n //= divisor
            else:
                divisor += 1
        return factors
    if len(numbers) > 790:
        return get_prime_factors(numbers[790])
    else:
        return set()