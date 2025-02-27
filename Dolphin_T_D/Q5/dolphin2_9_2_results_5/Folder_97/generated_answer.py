def all_neg_ints_inclusive(lst):
    s = 40
    e = 80
    neg_list = [i for i in lst[s:e + 1] if i < 0]
    if neg_list == []:
        return []
    else:
        return neg_list