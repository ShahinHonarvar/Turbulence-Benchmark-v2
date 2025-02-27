import math

def sum_of_divisors_in_range(x):
    """sum_of_divisors_in_range(x)
    Write a function called 'sum_of_divisors_in_range' that takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 45 and 72, both inclusive. If no such divisors exist in the specified range, the function should return 0.
    """
    sum = 0
    for i in range(45, 73):
        if x % i == 0:
            sum += i
    if sum == 0:
        return 0
    return sum