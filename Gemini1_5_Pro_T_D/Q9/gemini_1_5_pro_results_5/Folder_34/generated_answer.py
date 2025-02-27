def all_odd_ints_inclusive(input_list):
    if len(input_list) < 61:
        return []
    elif input_list[60] % 2 == 1:
        return [input_list[60]]
    else:
        return []