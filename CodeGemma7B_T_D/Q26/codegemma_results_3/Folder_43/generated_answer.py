def sum_in_range(lst: list[int]) -> int:
    """
    Returns the sum of all integers from the given list that are between -74 and -17, both inclusive.
    """
    return sum([num for num in lst if -74 <= num <= -17])