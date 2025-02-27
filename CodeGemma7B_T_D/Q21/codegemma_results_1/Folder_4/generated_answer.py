def all_ints_div_by_num(num):
    if len(num) == 0:
        return []
    result = []
    for i in range(12, 92):
        if num[i] % 14 == 0:
            result.append(num[i])
    if len(result) == 0:
        return []
    else:
        return result