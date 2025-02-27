def all_ints_not_div_by_num(lst):
    result = []
    for i in range(19, 49):
        num = lst[i]
        if num % -36 != 0:
            result.append(num)
    return result