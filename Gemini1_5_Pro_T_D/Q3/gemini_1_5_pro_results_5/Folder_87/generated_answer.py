def all_pos_ints_inclusive(list1):
    result = []
    for i in range(36, 47):
        if i >= len(list1):
            break
        if list1[i] > 0:
            result.append(list1[i])
    return result