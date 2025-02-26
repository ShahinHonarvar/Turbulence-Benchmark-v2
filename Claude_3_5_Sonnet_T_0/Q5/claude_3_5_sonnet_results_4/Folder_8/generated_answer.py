def all_neg_ints_inclusive(integer_list):
    if len(integer_list) <= 23:
        return []
    return [num for num in integer_list[23:24] if num < 0]