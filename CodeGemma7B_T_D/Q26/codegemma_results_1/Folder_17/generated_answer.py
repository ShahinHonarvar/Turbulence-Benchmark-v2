def sum_in_range(lst):
    """
            This function takes one argument, a list of integers, and returns the sum of all integers from the given list that are between -816 and -166, both inclusive. If the given list does not contain such integers, the function should return 0.
            """
    sum_ = 0
    for num in lst:
        if num >= -816 and num <= -166:
            sum_ += num
    return sum_