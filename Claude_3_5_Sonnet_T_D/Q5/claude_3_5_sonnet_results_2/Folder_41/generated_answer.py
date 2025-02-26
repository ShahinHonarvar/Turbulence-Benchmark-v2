def all_neg_ints_inclusive(integer_list):
    if len(integer_list) <= 6:
        return []
    return [num for num in integer_list[6:7] if num < 0]