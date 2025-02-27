def all_odd_ints_inclusive(lst):
    result = []
    for i in lst[82:87]:
        if i % 2 != 0:
            result.append(i)
    if not result:
        return []
    else:
        return result