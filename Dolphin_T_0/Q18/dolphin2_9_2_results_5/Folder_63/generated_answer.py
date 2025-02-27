def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for num in lst[30:51]:
        if num % 81 == 0 or num % 64 == 0:
            sum_nums += num
    return sum_nums if sum_nums != 0 else 0