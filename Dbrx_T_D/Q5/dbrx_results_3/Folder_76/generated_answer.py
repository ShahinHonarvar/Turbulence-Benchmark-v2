def all_neg_ints_inclusive(lst):
    if len(lst) < 987:
        return []
    result = []
    for i in range(686, 988):
        if lst[i] < 0:
            result.append(lst[i])
    return result