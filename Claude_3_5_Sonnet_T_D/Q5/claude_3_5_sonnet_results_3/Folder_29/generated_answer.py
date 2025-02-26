def all_neg_ints_inclusive(integer_list):
    if len(integer_list) < 98:
        return [num for num in integer_list[59:] if num < 0]
    else:
        return [num for num in integer_list[59:98] if num < 0]