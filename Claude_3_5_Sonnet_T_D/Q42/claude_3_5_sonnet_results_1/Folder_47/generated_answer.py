def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(num):
        factors = set()
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                if is_prime(i):
                    factors.add(i)
                if is_prime(num // i):
                    factors.add(num // i)
        if is_prime(num):
            factors.add(num)
        return factors
    if len(numbers) <= 34:
        return set()
    return get_factors(numbers[34])