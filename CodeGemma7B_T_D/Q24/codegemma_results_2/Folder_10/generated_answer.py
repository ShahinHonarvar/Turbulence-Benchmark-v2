def sum_of_divisors_in_range(x):
    """
    This function takes a positive integer as its argument, and returns the sum of
    all positive divisors of the given integer that are between 60 and 86, both
    inclusive. If no such divisors exist in the specified range, the function
    should return 0.
    """
    divider_sum = 0
    for num in range(60, 87):
        if x % num == 0:
            divider_sum += num
    if divider_sum == 0:
        return 0
    else:
        return divider_sum