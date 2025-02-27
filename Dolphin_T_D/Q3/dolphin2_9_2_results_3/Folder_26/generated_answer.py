def all_pos_ints_inclusive(input_list):
    if not input_list:
        return []
    result = [num for num in input_list[62:100] if num > 0]
    return result if result else []