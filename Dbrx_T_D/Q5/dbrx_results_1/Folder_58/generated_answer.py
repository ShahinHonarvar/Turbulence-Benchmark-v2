def all_neg_ints_inclusive(values):
    result = []
    for i in range(209, 557):
        if i < len(values) and values[i] < 0:
            result.append(values[i])
    return result