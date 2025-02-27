def all_ints_not_div_by_num(lst):
    result = []
    for i in range(17, 88):
        num = lst[i]
        if num % -75 != 0:
            result.append(num)
    return result