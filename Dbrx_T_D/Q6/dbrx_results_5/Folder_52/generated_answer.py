def all_neg_ints_exclusive(int_list):
    if len(int_list) <= 93:
        return []
    if int_list[93] < 0 and (len(int_list) == 94 or int_list[94] >= 0):
        return [int_list[93]]
    if int_list[94] < 0:
        return int_list[93:94]
    return []