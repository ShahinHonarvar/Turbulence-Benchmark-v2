def all_pos_ints_inclusive(input_list):
    if len(input_list) < 50:
        return []
    result = [i for i in input_list[22:51] if i > 0]
    return result