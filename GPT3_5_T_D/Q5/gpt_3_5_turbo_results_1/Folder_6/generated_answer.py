def all_neg_ints_inclusive(lst):
    negative_ints = []
    for i in range(10, 67):
        if lst[i] < 0:
            negative_ints.append(lst[i])
    return negative_ints