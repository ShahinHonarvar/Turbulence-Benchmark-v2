def all_neg_ints_inclusive(list):
    result = []
    for i in range(43, 52):
        if list[i] < 0:
            result.append(list[i])
    return result if result else []