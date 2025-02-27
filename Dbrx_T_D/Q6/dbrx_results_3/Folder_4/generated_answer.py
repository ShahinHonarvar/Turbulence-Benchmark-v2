def all_neg_ints_exclusive(input_list):
    if len(input_list) >= 77:
        start = 10
        end = 76
        return [i for i in input_list[start:end] if i < 0]
    else:
        return []