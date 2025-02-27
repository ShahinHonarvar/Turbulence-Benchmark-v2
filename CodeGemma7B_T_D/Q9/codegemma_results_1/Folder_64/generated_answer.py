def all_odd_ints_inclusive(l):
    result = []
    for i in range(0, 5):
        if l[i] % 2 != 0:
            result.append(l[i])
    return result