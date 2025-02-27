def all_odd_ints_inclusive(lst):
    result = []
    for i in range(40, 201):
        if i in lst and i % 2 != 0:
            result.append(i)
    return result