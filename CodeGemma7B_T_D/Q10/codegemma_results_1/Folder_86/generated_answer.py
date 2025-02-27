def all_odd_ints_exclusive(int_list):
    """
    The function takes one argument, a list of integers, and returns the list of all odd integers from index 18 to index 60, both exclusive.
    If no odd integers exist in the specified range, the function should return an empty list.
    """
    odd_ints = [x for x in int_list if x % 2 != 0]
    odd_ints_in_range = odd_ints[18:60]
    return odd_ints_in_range