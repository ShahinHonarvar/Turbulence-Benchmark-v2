def all_pos_ints_inclusive(int_list):
    result = []
    for i in range(686, 988):
        if i >= len(int_list) or int_list[i] <= 0:
            continue
        result.append(int_list[i])
    return result if result else []