def all_ints_not_div_by_num(num):
    result = []
    for i in range(199, 201):
        if num[i] % -200 != 0:
            result.append(num[i])
    return result