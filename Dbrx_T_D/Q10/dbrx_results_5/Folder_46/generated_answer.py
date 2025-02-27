def all_odd_ints_exclusive(lst):
    result = []
    for i in range(len(lst)):
        if i >= 20 and i < 43:
            if lst[i] % 2 != 0:
                result.append(lst[i])
    return result