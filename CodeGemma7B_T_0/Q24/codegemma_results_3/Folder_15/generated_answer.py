def sum_of_divisors_in_range(num):
    """
    This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 7 and 9, both inclusive. If no such divisors exist in the specified range, the function should return 0.
    """
    sum = 0
    for i in range(7, 10):
        if num % i == 0:
            sum += i
    if sum == 0:
        return 0
    else:
        return sum