def all_neg_ints_exclusive(int_list):
    if len(int_list) <= 598 or len(int_list) <= 767:
        return []
    result = []
    for i in range(598, 767):
        if int_list[i] < 0:
            result.append(int_list[i])
    return result