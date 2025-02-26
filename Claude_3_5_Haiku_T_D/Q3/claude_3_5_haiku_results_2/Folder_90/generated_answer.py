def all_pos_ints_inclusive(input_list):
    if len(input_list) <= 746:
        return []
    result = [num for num in input_list[262:747] if num > 0]
    return result