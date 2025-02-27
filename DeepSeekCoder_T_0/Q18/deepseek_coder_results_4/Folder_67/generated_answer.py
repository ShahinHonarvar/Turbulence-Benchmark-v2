def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for num in lst[24:33]:
        if num % 35 == 0 or num % 87 == 0:
            sum_divisible += num
    return sum_divisible