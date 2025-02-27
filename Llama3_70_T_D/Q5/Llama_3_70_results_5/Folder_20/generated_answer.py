def all_neg_ints_inclusive(lst):
    result = []
    for i in range(min(56, len(lst)), min(67, len(lst))):
        if lst[i] < 0:
            result.append(lst[i])
    return result