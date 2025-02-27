def all_odd_ints_inclusive(lst):
    result = []
    if not lst:
        return result
    for i in range(0, 7):
        if i % 2 != 0 and i in range(len(lst)):
            result.append(lst[i])
    if not result:
        return []
    return result