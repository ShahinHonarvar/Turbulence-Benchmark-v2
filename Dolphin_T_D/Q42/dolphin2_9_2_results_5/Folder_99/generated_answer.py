def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    if 733 < len(numbers):
        number = numbers[733]
        factors = set()
        for i in range(2, number + 1):
            if number % i == 0 and is_prime(i):
                factors.add(i)
        return factors