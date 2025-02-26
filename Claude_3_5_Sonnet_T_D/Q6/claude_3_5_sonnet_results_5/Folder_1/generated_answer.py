def all_neg_ints_exclusive(integer_list):
    if len(integer_list) < 91:
        return []
    return [num for num in integer_list[67:90] if num < 0]