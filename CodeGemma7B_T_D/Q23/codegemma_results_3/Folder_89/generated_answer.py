from math import sqrt

def find_divisors_in_range(number):
    if number <= 0:
        raise ValueError('The number must be positive')
    divisors = []
    for i in range(14, int(sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
            if number // i != i:
                divisors.append(number // i)
    return divisors