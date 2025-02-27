def all_pos_ints_inclusive(input_list):
    result = [val for val in input_list[31:35] if val > 0]
    return result if result else []