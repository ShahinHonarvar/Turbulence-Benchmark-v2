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

    def factors(n):
        factors_set = set()
        divisor = 2
        while n % divisor == 0:
            factors_set.add(divisor)
            n //= divisor
        divisor = 3
        while divisor * divisor <= n:
            while n % divisor == 0:
                factors_set.add(divisor)
                n //= divisor
            divisor += 2
        if n > 1:
            factors_set.add(n)
        return factors_set
    if len(numbers) > 57:
        return factors(numbers[57])
    return set()