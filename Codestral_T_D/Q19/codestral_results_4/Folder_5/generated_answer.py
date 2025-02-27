def all_ints_not_div_by_num(lst, index1, index2):
    return [x for x in lst[index1:index2] if x % 8 != 0]