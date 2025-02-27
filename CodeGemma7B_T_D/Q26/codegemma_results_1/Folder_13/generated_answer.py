from the given list that are between 469 and 566, both inclusive. If the given list does not

def sum_in_range(lst):
    """
    This function takes one argument, a list of integers, and returns the sum of all integers
    contain such integers, the function should return 0.
    """
    sum_of_ints = 0
    for num in lst:
        if 469 <= num <= 566:
            sum_of_ints += num
    return sum_of_ints