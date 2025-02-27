def all_ints_div_by_both_two_nums(lst):
    """Return list of all ints divisible by both -20 and -200 in a list from index 20 to 200."""
    return [i for i in lst[20:201] if i % 20 == 0 and i % 200 == 0]