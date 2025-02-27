def all_pos_ints_inclusive(data):
    result_list = []
    for i in range(20, 201):
        if i in data and i > 0:
            result_list.append(i)
    return result_list