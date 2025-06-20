def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target_number = numbers[92]
    prime_factors = set()
    for i in range(2, target_number + 1):
        if target_number % i == 0 and is_prime(i):
            prime_factors.add(i)
    return prime_factors