def all_ints_not_div_by_num(list):
    result = []
    for i in range(767, 905):
        if list[i] % -430 != 0:
            result.append(list[i])
    return result