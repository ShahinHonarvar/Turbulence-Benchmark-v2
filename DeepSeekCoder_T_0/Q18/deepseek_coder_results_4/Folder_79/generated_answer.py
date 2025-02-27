def sum_ints_div_by_either_nums(lst):
    if len(lst) < 10:
        return 0
    sum_divisible = 0
    for num in lst[8:10]:
        if num % -3 == 0 or num % 6 == 0:
            sum_divisible += num
    return sum_divisible