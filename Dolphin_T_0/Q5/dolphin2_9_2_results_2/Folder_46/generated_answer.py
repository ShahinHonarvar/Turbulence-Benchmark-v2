def all_neg_ints_inclusive(lst):
    neg_nums = []
    for i in range(30, 88):
        if lst[i] < 0:
            neg_nums.append(lst[i])
    return neg_nums