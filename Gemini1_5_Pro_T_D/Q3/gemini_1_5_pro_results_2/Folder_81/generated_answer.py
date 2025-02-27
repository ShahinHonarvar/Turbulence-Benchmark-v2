def all_pos_ints_inclusive(lst):
    result = []
    if len(lst) > 100:
        for i in range(10, 101):
            if lst[i] > 0:
                result.append(lst[i])
    else:
        for i in range(len(lst)):
            if i >= 10 and lst[i] > 0:
                result.append(lst[i])
    return result