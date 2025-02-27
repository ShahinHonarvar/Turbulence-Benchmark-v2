def all_neg_ints_inclusive(lst):
    if len(lst) < 200:
        return []
    result = []
    for i in range(90, 201):
        if lst[i] < 0:
            result.append(lst[i])
    return result