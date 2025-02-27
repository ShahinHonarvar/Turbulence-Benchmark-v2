def all_ints_not_div_by_num(int_list):
    """
    Returns a list of all integers not divisible by 40 from index 20 to index 50 (exclusive).
    """
    return [i for i in int_list[20:50] if i % 40 != 0]