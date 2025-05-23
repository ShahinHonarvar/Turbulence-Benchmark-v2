def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    num = numbers[6]
    for i in range(2, num + 1):
        while num % i == 0 and is_prime(i):
            factors.add(i)
            num = num // i
    return factors