def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    number = numbers[66]
    factors = set()
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            factors.add(i)
            number //= i
    if number > 1:
        factors.add(number)
    return factors