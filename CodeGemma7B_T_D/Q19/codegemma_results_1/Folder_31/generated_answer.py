def all_ints_not_div_by_num(lst):
    """
    Returns a list of all integers in a list not divisible by -67 from index 18 to index 37, both exclusive.
    If no such integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in lst[18:37] if num % -67 != 0]