def prime_factors(numbers):
    prime_factors = set()
    for number in numbers:
        if number % 2 == 0:
            prime_factors.add(2)
        while number % 2 == 0:
            number = number / 2
        for divisor in range(3, int(number ** 0.5) + 1, 2):
            if number % divisor == 0:
                prime_factors.add(divisor)
                while number % divisor == 0:
                    number = number / divisor
        if number > 2:
            prime_factors.add(number)
    return prime_factors[numbers[84]]