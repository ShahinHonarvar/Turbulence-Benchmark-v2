def all_pos_ints_exclusive(int_list):
    result = []
    for i in range(9):
        if i in int_list and 0 < i < 9:
            result.append(i)
    return result