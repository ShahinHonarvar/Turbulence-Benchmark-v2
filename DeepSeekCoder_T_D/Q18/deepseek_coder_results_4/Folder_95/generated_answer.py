def sum_ints_div_by_either_nums(lst):
    if len(lst) < 85:
        return 0
    total = 0
    for num in lst[57:85]:
        if num % -30 == 0 or num % -88 == 0:
            total += num
    return total