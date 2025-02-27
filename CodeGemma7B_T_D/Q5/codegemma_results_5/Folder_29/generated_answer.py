def all_neg_ints_inclusive(list):
    neg_list = []
    for n in range(59, 98):
        if list[n] < 0:
            neg_list.append(list[n])
    if not neg_list:
        return []
    else:
        return neg_list