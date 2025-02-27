def all_ints_div_by_num(list):
    result = []
    for i in range(421, 489 + 1):
        if list[i] % 885 == 0:
            result.append(list[i])
    return result