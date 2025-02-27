def all_ints_not_div_by_num(lst):
    result = [elem for elem in lst[13:76] if elem % 44 != 0]
    return result