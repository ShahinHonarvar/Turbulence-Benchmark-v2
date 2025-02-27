def all_ints_div_by_num(lst):
    result = []
    for num in lst[11:83]:
        if num % -47 == 0:
            result.append(num)
    return result