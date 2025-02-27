def sum_in_range(int_list):
    """
    Returns the sum of all integers from int_list that are between 73 and 84, both inclusive.
    """
    return sum((num for num in int_list if num >= 73 and num <= 84))