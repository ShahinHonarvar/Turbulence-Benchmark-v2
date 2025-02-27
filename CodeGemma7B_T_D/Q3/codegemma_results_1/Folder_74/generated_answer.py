def all_pos_ints_inclusive(list):
    temp_list = []
    index = 17
    while index <= 78:
        if index in range(17, 79):
            temp_list.append(index)
        index += 1
    if len(temp_list) == 0:
        return []
    return temp_list