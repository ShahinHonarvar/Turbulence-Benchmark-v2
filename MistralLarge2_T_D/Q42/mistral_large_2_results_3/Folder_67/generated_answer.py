def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors_set = set()
        for i in range(2, n + 1):
            while n % i == 0:
                factors_set.add(i)
                n //= i
        return factors_set
    if len(numbers) > 43:
        number = numbers[43]
        prime_factors_set = set(filter(is_prime, factors(number)))
        return prime_factors_set
    else:
        return set()