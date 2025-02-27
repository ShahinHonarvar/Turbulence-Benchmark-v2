def all_even_ints_inclusive(lst):
    if len(lst) < 67:
        return []
    result = []
    for i in range(64, 67):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result