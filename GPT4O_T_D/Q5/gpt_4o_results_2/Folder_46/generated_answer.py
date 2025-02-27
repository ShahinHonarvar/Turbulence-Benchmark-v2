def all_neg_ints_inclusive(int_list):
    if len(int_list) < 88:
        return []
    return [num for num in int_list[30:88] if num < 0]