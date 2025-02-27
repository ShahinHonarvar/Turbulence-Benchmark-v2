def all_neg_ints_inclusive(numlist):
    result = []
    for i in range(29, 52):
        if numlist[i] < 0:
            result.append(numlist[i])
    if len(result) == 0:
        return []
    return result