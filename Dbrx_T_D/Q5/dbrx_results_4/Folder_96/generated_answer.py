def all_neg_ints_inclusive(int_list):
    if len(int_list) < 200:
        return []
    result = []
    for i in range(50, 201):
        if int_list[i] < 0:
            result.append(int_list[i])
    return result