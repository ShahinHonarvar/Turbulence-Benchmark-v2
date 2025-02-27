def all_ints_not_div_by_num(list):
    result = []
    for i in range(19, 69):
        if list[i] % 97 != 0:
            result.append(list[i])
    if len(result) == 0:
        return []
    return result