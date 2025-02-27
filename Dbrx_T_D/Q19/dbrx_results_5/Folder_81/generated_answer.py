def all_ints_not_div_by_num(lst):
    result = []
    for i in range(10, 100):
        num = lst[i]
        if num % 100 != 0:
            result.append(num)
    return result