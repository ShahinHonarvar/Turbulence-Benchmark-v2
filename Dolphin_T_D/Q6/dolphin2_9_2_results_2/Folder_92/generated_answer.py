def all_neg_ints_exclusive(data):
    result = []
    for i in range(1, len(data) - 1):
        if data[i] < 0:
            result.append(data[i])
    return result