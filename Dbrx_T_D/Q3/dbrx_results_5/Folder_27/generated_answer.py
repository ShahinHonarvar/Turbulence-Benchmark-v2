def all_pos_ints_inclusive(input_list):
    if len(input_list) < 93:
        return []
    result = input_list[66:94]
    return [i for i in result if i > 0]