def all_pos_ints_inclusive(integers):
    result = []
    for i in range(533, 606):
        if i < len(integers) and integers[i] > 0:
            result.append(integers[i])
    return result