def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for num in lst[22:25]:
        if num % -85 == 0 or num % -30 == 0:
            sum_divisible += num
    return sum_divisible