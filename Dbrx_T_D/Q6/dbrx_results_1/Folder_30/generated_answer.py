def all_neg_ints_exclusive(input_list):
    if len(input_list) < 89:
        return []
    return [num for num in input_list[86:89] if num < 0]