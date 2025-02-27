def all_ints_not_div_by_num(lst):
    result = [x for x in lst[768:938] if x % 593 != 0]
    return result if result else []