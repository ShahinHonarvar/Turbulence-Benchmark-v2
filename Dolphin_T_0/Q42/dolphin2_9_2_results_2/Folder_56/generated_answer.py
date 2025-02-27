def prime_factors(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factorized = set()
    for num in numbers[60]:
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                factorized.add(i)
    return factorized