def prime_factors(numbers):
    prime_factors = set()
    for number in numbers:
        if number % 42 == 0 and number != 42:
            prime_factors.add(number)
    return prime_factors