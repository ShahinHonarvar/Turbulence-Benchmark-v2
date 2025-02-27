from math import sqrt

def sum_of_divisors_in_range(x):
    sum_div = 0
    limit = int(sqrt(x)) + 1
    for divisor in range(35, limit):
        if x % divisor == 0 and divisor in range(35, 99):
            sum_div += divisor
            if divisor != x // divisor:
                sum_div += x // divisor
    return sum_div