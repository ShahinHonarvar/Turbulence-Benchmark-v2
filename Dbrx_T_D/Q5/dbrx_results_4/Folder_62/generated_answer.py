def all_neg_ints_inclusive(input_list):
    if len(input_list) < 99:
        return []
    neg_ints = [num for num in input_list[90:100] if num < 0]
    return neg_ints