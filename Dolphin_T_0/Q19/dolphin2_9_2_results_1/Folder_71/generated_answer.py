def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[22:51]:
        if num % -77 != 0:
            result.append(num)
    return result