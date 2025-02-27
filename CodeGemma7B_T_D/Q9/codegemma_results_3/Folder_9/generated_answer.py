def all_odd_ints_inclusive(lst):
    result = []
    for i in range(70, 201):
        if i % 2 != 0:
            result.append(lst[i])
    return result