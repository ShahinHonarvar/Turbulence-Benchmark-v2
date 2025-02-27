def all_odd_ints_inclusive(list):
    result = []
    for i in range(533, 606):
        if i % 2 != 0:
            result.append(i)
    if not result:
        return []
    else:
        return result