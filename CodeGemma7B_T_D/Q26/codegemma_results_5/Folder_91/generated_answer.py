def sum_in_range(lst):
    """
    This function takes one argument, a list of integers, and returns the sum of all integers from the given list that are between -8 and 8, both inclusive. If the given list does not contain such integers, the function should return 0.
    """
    return sum((x for x in lst if -8 <= x <= 8))