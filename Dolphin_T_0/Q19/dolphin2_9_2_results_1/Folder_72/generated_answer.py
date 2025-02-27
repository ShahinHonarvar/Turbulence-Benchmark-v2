def all_ints_not_div_by_num(ints):
    result = []
    for i in range(13, 70):
        if ints[i] % -78 != 0:
            result.append(ints[i])
    return result