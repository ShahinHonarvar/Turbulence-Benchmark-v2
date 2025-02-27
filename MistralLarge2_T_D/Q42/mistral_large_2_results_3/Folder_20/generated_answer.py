def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if len(numbers) <= 53:
        return set()
    number = numbers[53]
    factors = set()
    for i in range(2, number + 1):
        while number % i == 0 and is_prime(i):
            factors.add(i)
            number //= i
    return factors