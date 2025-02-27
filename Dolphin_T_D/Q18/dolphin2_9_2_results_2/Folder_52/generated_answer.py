def sum_ints_div_by_either_nums(lst):
    s = 0
    for num in lst[47:60]:
        if num % 88 == 0 or num % 58 == 0:
            s += num
    return s