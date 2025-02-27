def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for num in lst[828:933]:
        if num % -649 == 0 or num % -461 == 0:
            sum_divisible += num
    return sum_divisible