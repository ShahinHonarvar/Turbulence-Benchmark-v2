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
        while n % 2 == 0:
            factors_set.add(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                factors_set.add(i)
                n //= i
        if n > 2:
            factors_set.add(n)
        return {factor for factor in factors_set if is_prime(factor)}
    return factors(numbers[60]) if len(numbers) > 60 else set()