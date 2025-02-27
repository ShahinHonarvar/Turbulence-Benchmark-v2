def all_pos_ints_inclusive(x):
    result = []
    for i in range(3, 6):
        if i in x:
            result.append(i)
    return result