def all_neg_ints_inclusive(input_list):
    if len(input_list) < 87:
        return []
    return [i for i in input_list[82:87] if i < 0]