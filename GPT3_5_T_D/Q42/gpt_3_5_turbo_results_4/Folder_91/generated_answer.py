def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = numbers[6]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
    return factors