def all_neg_ints_exclusive(int_list):
    if len(int_list) < 40:
        return []
    result = []
    for i in range(15, 40):
        if int_list[i] < 0:
            result.append(int_list[i])
    return result