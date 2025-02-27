def all_neg_ints_inclusive(int_list):
    if len(int_list) < 52:
        return []
    result = []
    for i in range(29, 52):
        if int_list[i] < 0:
            result.append(int_list[i])
    return result