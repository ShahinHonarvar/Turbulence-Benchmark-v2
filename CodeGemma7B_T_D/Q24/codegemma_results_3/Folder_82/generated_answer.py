from math import sqrt

def sum_of_divisors_in_range(number):
    """Summing divisors in a specified range."""
    sum = 0
    for i in range(4, int(sqrt(number)) + 1):
        if number % i == 0:
            sum += i
            if i != number // i:
                sum += number // i
    return sum