def all_neg_ints_inclusive(int_list):
    result = []
    if len(int_list) > 0 and int_list[0] < 0:
        result.append(int_list[0])
    return result