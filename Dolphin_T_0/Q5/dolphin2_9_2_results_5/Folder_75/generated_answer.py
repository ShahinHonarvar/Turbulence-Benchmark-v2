def all_neg_ints_inclusive(lst):
    neg_nums = []
    for i in range(56, 58):
        if lst[i] < 0:
            neg_nums.append(lst[i])
    return neg_nums