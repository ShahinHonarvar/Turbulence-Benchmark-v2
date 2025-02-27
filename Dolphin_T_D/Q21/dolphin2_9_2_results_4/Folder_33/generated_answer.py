def all_ints_div_by_num(lst):
    result = []
    for num in lst[319:613]:
        if num % -215 == 0:
            result.append(num)
    return result