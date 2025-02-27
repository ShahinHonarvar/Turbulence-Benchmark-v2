def all_pos_ints_inclusive(list_of_ints):
    result = []
    for i in range(12, 93):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] > 0:
            result.append(list_of_ints[i])
    return result