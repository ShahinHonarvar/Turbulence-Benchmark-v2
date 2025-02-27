def all_odd_ints_exclusive(lst):
    result = []
    for i in range(len(lst)):
        if i >= 0 and i < 4:
            if lst[i] % 2 != 0:
                result.append(lst[i])
    return result