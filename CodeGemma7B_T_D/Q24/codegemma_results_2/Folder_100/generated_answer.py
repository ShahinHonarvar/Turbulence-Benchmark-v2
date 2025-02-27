from functools import reduce

def sum_of_divisors_in_range(num):
    """This function takes a positive integer as its argument and returns the sum of all positive divisors of the given integer that are between 11 and 41, both inclusive. If no such divisors exist in the specified range, the function should return 0."""
    if num < 11 or num > 41:
        return 0
    divisors = reduce(lambda x, y: x + y, (i for i in range(1, num + 1) if num % i == 0 and 11 <= i <= 41))
    return divisors