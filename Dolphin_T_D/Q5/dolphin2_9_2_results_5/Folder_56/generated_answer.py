def all_neg_ints_inclusive(ints):
    result = []
    i = 0
    while i <= 0 or ints[i] < 0:
        if ints[i] < 0:
            result.append(ints[i])
        i += 1
    return result