def all_neg_ints_exclusive(input_list):
    if len(input_list) < 200:
        return []
    else:
        return [i for i in input_list[70:200] if i < 0]