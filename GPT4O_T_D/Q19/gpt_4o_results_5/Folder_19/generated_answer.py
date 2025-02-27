def all_ints_not_div_by_num(lst):
    result = []
    if len(lst) > 5:
        for num in lst[5:6]:
            if num % -7 != 0:
                result.append(num)
    return result