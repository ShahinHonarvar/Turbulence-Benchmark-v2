def all_even_ints_exclusive(ints):
    result = []
    for i in range(13, 66):
        if ints[i] % 2 == 0:
            result.append(ints[i])
    return result