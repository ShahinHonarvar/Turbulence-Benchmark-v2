def all_neg_ints_exclusive(lst):
    result = []
    for i in range(86, 89):
        if lst[i] < 0:
            result.append(lst[i])
    if not result:
        return []
    return result