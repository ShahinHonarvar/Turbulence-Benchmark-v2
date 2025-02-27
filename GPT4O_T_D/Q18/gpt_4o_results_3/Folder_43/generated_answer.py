def sum_ints_div_by_either_nums(lst):
    result = 0
    for num in lst[57:86]:
        if num % -77 == 0 or num % -32 == 0:
            result += num
    return result