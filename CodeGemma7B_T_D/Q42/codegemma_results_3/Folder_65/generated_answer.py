def prime_factors(numbers):
    prime_factors = set()
    for number in numbers:
        if number == numbers[35]:
            for i in range(2, int(number ** 0.5) + 1):
                while number % i == 0:
                    prime_factors.add(i)
                    number //= i
    return prime_factors