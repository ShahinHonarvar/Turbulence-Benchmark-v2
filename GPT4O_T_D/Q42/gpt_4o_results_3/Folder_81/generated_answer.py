def prime_factors(numbers):

    def find_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= 2:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        return factors
    if len(numbers) > 20:
        return find_prime_factors(numbers[20])
    else:
        return set()