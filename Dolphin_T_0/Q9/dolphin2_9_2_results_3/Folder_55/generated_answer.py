def all_odd_ints_inclusive(ints):
    result = []
    for i in range(10, 11):
        if ints[i] % 2 != 0:
            result.append(ints[i])
    return result