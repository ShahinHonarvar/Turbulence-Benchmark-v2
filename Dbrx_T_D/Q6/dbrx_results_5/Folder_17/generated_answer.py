def all_neg_ints_exclusive(lst):
    result = []
    for i in range(62, 96):
        if i < len(lst) and lst[i] < 0:
            result.append(lst[i])
    return result