def all_neg_ints_inclusive(lst):
    result = []
    for i in range(50, 55):
        if lst[i] < 0:
            result.append(lst[i])
    return result