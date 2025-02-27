def all_odd_ints_inclusive(lst):
    result = []
    for i in range(0, lst[0] + 1):
        if i % 2 != 0:
            result.append(i)
    return result