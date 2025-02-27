def all_ints_div_by_num(ints):
    result = []
    for i in range(30, 60):
        if ints[i] % 39 == 0:
            result.append(ints[i])
    return result