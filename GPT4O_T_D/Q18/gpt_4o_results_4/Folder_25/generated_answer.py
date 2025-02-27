def sum_ints_div_by_either_nums(lst):
    if not lst or len(lst) < 80:
        return 0
    s = 0
    for num in lst[25:81]:
        if num % -20 == 0 or num % -26 == 0:
            s += num
    return s