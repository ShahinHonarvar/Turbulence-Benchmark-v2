def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                if is_prime(i):
                    factors.add(i)
                num //= i
        if num > 1 and is_prime(num):
            factors.add(num)
        return factors
    if len(numbers) <= 49:
        return set()
    return get_prime_factors(numbers[49])