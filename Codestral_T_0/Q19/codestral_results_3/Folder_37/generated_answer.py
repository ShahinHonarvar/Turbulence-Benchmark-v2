def all_ints_not_div_by_num(lst, index1, index2):
    return [i for i in lst[index1:index2] if i % 5 != 0]