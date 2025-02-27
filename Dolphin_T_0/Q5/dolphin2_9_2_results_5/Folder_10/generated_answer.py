def all_neg_ints_inclusive(lst):
    sliced_lst = lst[25:60]
    result = [i for i in sliced_lst if i < 0]
    return result