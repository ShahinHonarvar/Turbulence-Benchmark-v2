def sum_in_range(lst):
    """Returns the sum of all integers in the given list between 20 and 93, inclusive."""
    return sum([x for x in lst if 20 <= x <= 93])