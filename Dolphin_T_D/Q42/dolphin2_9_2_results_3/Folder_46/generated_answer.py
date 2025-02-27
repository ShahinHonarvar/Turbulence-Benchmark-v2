def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    target_number = numbers[453]
    factors = set()
    for i in range(2, target_number + 1):
        if target_number % i == 0 and is_prime(i):
            factors.add(i)
    return factors