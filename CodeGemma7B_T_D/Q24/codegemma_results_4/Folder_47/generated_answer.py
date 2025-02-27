from math import sqrt

def sum_of_divisors_in_range(number):
    sum = 0
    for i in range(27, 45):
        if number % i == 0:
            sum += i
    if sum == 0:
        sum = 0
    return sum