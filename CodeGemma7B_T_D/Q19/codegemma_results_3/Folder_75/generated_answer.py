def all_ints_not_div_by_num(lst):
    """Returns a list of integers not divisible by -48 from index 20 to index 51, both exclusive."""
    return [x for x in lst[20:51] if x % -48 != 0]