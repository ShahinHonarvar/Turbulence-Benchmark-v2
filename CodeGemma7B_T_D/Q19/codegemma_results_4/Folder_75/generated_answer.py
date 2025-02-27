def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[20:51]:
        if num % -48 != 0:
            result.append(num)
    return result if result else []