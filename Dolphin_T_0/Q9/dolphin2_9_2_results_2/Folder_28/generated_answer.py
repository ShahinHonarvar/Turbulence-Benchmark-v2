def all_odd_ints_inclusive(lst):
    result = []
    for i in range(62, 64):
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result if result else []