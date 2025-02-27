def all_neg_ints_inclusive(lst):
    if len(lst) < 605:
        return []
    result = []
    for i in range(533, 606):
        if isinstance(lst[i], int) and lst[i] < 0:
            result.append(lst[i])
    return result