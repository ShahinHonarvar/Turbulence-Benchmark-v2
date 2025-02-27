def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[16:87]:
        if num % -15 != 0:
            result.append(num)
    return result