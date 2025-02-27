def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in lst[2:8]:
        if i % -1 == 0 or i % -7 == 0:
            result += i
    if result == 0:
        return 0
    else:
        return result