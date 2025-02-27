def all_neg_ints_exclusive(integer_list):
    if len(integer_list) < 90:
        return []
    result = []
    for i in range(86, 90):
        if integer_list[i] < 0:
            result.append(integer_list[i])
    return result