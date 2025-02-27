def all_neg_ints_exclusive(input_list):
    if len(input_list) < 80:
        return []
    else:
        return [num for num in input_list[10:80] if num < 0]