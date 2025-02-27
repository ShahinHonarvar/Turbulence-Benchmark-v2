def all_odd_ints_exclusive(ints):
    result = []
    for i in range(81, 200):
        if i >= len(ints):
            break
        if ints[i] % 2 != 0:
            result.append(ints[i])
    return result