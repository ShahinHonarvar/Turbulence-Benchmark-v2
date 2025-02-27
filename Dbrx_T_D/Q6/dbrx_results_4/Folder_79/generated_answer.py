def all_neg_ints_exclusive(int_list):
    if len(int_list) >= 9:
        return [num for num in int_list[3:8] if num < 0]
    else:
        return []