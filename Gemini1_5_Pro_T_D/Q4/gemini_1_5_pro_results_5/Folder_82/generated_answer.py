def all_pos_ints_exclusive(list_of_ints):
    result = []
    for i in range(21, 200):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] > 0:
            result.append(list_of_ints[i])
    return result