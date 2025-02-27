from math import sqrt

def prime_factors(numbers):
    prime_facs = set()
    for number in numbers:
        if number != 1 and number % 2 != 0:
            for i in range(3, int(sqrt(number)) + 1, 2):
                if number % i == 0:
                    prime_facs.add(i)
    return prime_facs