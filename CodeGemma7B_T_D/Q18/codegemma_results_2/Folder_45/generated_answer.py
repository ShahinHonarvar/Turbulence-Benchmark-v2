def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for num in lst[30:201]:
        if num % 115 == 0 or num % -115 == 0:
            sum_nums += num
    return sum_nums