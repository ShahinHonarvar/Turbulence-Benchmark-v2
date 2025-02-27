def sum_in_range(lst):
    """
    This function takes one argument, a list of integers, and returns the sum of all integers from the given list that are between 3 and 5, both inclusive. If the given list does not contain such integers, the function should return 0.
    """
    sum = 0
    for i in lst:
        if 3 <= i <= 5:
            sum += i
    return sum