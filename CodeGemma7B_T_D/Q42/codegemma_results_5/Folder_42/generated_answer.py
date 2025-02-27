from math import sqrt

def prime_factors(numbers):
    prime_factors = set()
    number = numbers[276]
    for i in range(2, int(sqrt(number)) + 1):
        while number % i == 0:
            prime_factors.add(i)
            number //= i
    if number != 1:
        prime_factors.add(number)
    return prime_factors