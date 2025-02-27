def all_pos_ints_inclusive(lst):
    result = []
    for i in range(10, 101):
        if 0 <= i < len(lst) and lst[i] > 0:
            result.append(lst[i])
    return result