def all_pos_ints_inclusive(input_list):
    if len(input_list) <= 97:
        return []
    subset = input_list[59:98]
    return [num for num in subset if num > 0]