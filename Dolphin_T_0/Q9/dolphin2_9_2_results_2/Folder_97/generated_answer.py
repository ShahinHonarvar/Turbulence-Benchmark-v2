def all_odd_ints_inclusive(lst):
    result = []
    for index in range(40, 81):
        if lst[index] % 2 != 0:
            result.append(lst[index])
    return result