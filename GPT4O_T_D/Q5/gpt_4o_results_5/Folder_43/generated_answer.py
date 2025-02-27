def all_neg_ints_inclusive(int_list):
    if len(int_list) < 87:
        return []
    return [num for num in int_list[68:87] if num < 0]