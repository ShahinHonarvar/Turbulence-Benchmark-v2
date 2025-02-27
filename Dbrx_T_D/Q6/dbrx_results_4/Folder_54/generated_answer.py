def all_neg_ints_exclusive(input_list):
    if len(input_list) >= 35:
        return [num for num in input_list[27:34] if num < 0]
    else:
        return []