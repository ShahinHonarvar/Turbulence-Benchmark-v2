def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    number = numbers[59]
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