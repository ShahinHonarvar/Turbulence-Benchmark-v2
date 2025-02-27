def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    number = numbers[19]
    factors = set()
    while number % 2 == 0:
        factors.add(2)
        number = number // 2
    for i in range(3, int(number ** 0.5) + 1, 2):
        while number % i == 0:
            factors.add(i)
            number = number // i
    if number > 2:
        factors.add(number)
    return factors