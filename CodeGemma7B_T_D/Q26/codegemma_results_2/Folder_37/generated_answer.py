def sum_in_range(lst):
    """
    Returns the sum of all  integers from the given list that
    are between 1 and 8, both inclusive.
    """
    sum_in_range_list = [i for i in lst if 8 >= i >= 1]
    return sum(sum_in_range_list)