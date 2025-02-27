def all_pos_ints_inclusive(lst):
    result = []
    for i in range(10, 101):
        if i in lst and i >= 0:
            result.append(i)
    return result