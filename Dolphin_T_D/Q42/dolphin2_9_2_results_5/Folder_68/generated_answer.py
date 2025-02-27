def prime_factors(numbers):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        squarerootn = int(n ** 0.5) + 1
        for divisor in range(3, squarerootn, 2):
            if n % divisor == 0:
                return False
        return True
    number = numbers[3]
    prime_factors_set = set()
    for factor in range(2, number + 1):
        if is_prime(factor) and number % factor == 0:
            prime_factors_set.add(factor)
    return prime_factors_set