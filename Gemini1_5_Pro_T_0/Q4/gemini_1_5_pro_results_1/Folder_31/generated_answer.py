def all_pos_ints_exclusive(list_of_ints):
    result = []
    for i in range(87, 95):
        if i >= len(list_of_ints) or i < 0:
            break
        if list_of_ints[i] > 0:
            result.append(list_of_ints[i])
    return result