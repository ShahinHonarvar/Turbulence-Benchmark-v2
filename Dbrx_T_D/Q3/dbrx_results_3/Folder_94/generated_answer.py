def all_pos_ints_inclusive(input_list):
    if len(input_list) < 41 or len(input_list) > 100:
        return []
    pos_ints = []
    index = 28
    while index <= 40:
        if input_list[index] > 0:
            pos_ints.append(input_list[index])
        index += 1
    return pos_ints