def all_pos_ints_inclusive(input_list):
    if len(input_list) < 64:
        return []
    positive_integers = [num for num in input_list[22:64] if num > 0]
    return positive_integers