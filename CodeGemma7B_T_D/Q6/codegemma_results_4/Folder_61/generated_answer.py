def all_neg_ints_exclusive(list):
    filtered_list = [number for number in list if number < 0 and number > -8]
    return filtered_list or []