def all_neg_ints_inclusive(int_list):
    result = []
    for x in int_list[30:49]:
        if x < 0:
            result.append(x)
    return result or []