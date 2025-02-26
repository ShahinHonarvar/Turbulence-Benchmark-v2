def all_pos_ints_inclusive(input_list):
    if len(input_list) < 87:
        return []
    result = [num for num in input_list[68:87] if num > 0]
    return result