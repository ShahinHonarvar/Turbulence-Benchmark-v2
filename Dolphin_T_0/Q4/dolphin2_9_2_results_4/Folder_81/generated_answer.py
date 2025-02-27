def all_pos_ints_exclusive(int_list):
    result = []
    for i in int_list[10:100]:
        if i > 0:
            result.append(i)
    return result