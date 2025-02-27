def all_ints_not_div_by_num(lst):
    result = [i for i in lst[767:938] if i % 593 != 0]
    return result if result else []