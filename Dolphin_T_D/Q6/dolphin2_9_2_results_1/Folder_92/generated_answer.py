def all_neg_ints_exclusive(lst):
    result = []
    for i in range(2, len(lst)):
        if lst[i] < 0:
            result.append(lst[i])
    return result