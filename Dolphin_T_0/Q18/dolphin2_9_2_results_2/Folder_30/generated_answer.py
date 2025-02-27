def sum_ints_div_by_either_nums(lst):
    sum_res = 0
    for num in lst[10:76]:
        if num % -81 == 0 or num % -94 == 0:
            sum_res += num
    return sum_res