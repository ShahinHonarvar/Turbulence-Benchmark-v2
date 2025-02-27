def all_pos_ints_inclusive(integer_list):
    output = []
    for i in range(22, 64):
        if i in integer_list:
            output.append(i)
    return output or []