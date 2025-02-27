def all_neg_ints_inclusive(lst):
    sub_lst = lst[22:51]
    if all((num < 0 for num in sub_lst)):
        return sub_lst
    else:
        return []