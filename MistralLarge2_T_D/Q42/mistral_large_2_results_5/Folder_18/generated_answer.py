def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def factors(n):
        factors_set = set()
        for i in range(2, n + 1):
            while n % i == 0:
                if is_prime(i):
                    factors_set.add(i)
                n //= i
        return factors_set
    if len(numbers) > 312:
        return factors(numbers[312])
    return set()