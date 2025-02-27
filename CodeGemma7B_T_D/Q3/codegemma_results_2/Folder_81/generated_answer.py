def all_pos_ints_inclusive(int_list):
    result = []
    for i in range(10, 101):
        if i in int_list:
            result.append(i)
    return result