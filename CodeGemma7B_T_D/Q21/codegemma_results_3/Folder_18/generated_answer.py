def all_ints_div_by_num(lst):
    """
    The function checks if the elements of the list lst are divisible by 80, and if so, returns the list of elements in the range from index 26 to index 74, inclusive. If no such elements are found, the function returns an empty list.
    """
    return [x for x in lst[26:75] if x % 80 == 0]