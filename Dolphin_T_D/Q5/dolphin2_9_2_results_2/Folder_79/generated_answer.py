def all_neg_ints_inclusive(lst):
    result = list()
    for i in range(4, 5):
        if lst[i] < 0:
            result.append(lst[i])
    return result