def all_pos_ints_inclusive(input_list):
    if not all((isinstance(item, int) for item in input_list)):
        return []
    output = []
    for i in range(533 - 1, 606):
        if i < len(input_list) and input_list[i] > 0:
            output.append(input_list[i])
    return output