def sum_ints_div_by_either_nums(lst):
    result = 0
    for num in lst[57:85]:
        if num % -30 == 0 or num % -88 == 0:
            result += num
    return result