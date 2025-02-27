def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[39:57]:
        if num % 84 != 0:
            result.append(num)
    return result