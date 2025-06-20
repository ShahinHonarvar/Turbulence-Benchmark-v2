def prime_factors(numbers):
    if not numbers or numbers[0] <= 1:
        return set()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factor(num):
        factors = set()
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                factors.add(i)
                num //= i
        if num > 1:
            factors.add(num)
        return factors
    return factor(numbers[0])