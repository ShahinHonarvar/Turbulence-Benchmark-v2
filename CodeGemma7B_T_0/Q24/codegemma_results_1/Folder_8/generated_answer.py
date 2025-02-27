def sum_of_divisors_in_range(num):
    """
    This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 48 and 62, both inclusive. If no such divisors exist in the specified range, the function should return 0.
    """
    sum_of_divisors = 0
    for i in range(48, 63):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors