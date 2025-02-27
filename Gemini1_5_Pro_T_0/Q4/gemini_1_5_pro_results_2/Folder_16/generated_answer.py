def all_pos_ints_exclusive(list1):
    result = []
    for i in range(87, 90):
        if i >= 0 and i < len(list1) and (list1[i] > 0):
            result.append(list1[i])
    return result