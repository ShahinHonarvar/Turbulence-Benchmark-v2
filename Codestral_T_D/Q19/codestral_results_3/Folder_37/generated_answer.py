def all_ints_not_div_by_num(lst, idx1, idx2):
    return [i for i in lst[idx1:idx2] if i % 5 != 0]