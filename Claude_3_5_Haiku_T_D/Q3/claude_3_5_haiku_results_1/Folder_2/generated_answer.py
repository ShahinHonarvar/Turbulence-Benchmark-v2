def all_pos_ints_inclusive(input_list):
    if len(input_list) <= 39:
        return []
    positive_ints = [num for num in input_list[15:40] if num > 0]
    return positive_ints