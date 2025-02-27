def all_odd_ints_inclusive(list):
    result = []
    for i in range(29, 94):
        if i % 2 != 0:
            result.append(i)
    return result