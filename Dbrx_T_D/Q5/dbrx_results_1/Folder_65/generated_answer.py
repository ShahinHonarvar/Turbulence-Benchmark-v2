def all_neg_ints_inclusive(a_list):
    if len(a_list) < 98:
        return []
    neg_ints = []
    for i in range(56, 99):
        if a_list[i] < 0:
            neg_ints.append(a_list[i])
    return neg_ints