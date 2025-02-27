def prime_factors(numbers):

    def find_prime_factors(n):
        factors = set()
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
            if divisor * divisor > n:
                if n > 1:
                    factors.add(n)
                break
        return factors
    if len(numbers) > 3:
        return find_prime_factors(numbers[3])
    return set()