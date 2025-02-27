def all_neg_ints_inclusive(list):
    result = []
    for i in range(37, 76):
        if list[i] < 0:
            result.append(list[i])
    if not result:
        result = []
    return result