def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for num in lst[240:902]:
        if num % 546 == 0 or num % 709 == 0:
            sum_divisible += num
    return sum_divisible