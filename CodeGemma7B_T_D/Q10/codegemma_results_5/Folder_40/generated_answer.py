def all_odd_ints_exclusive(lst):
    result = []
    for i in range(0, 3):
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result