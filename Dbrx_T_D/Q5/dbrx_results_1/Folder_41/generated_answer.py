def all_neg_ints_inclusive(int_list):
    if len(int_list) >= 13 and int_list[6] < 0 and (int_list[10] < 0):
        return [num for num in int_list[6:11] if num < 0]
    elif len(int_list) >= 13 and int_list[6] < 0 and (int_list[10] >= 0):
        return [int_list[6]]
    elif len(int_list) >= 13 and int_list[6] >= 0 and (int_list[10] < 0):
        return [int_list[10]]
    else:
        return []