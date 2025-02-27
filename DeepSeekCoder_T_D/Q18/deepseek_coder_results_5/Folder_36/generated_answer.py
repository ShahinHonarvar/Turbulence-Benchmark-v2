def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for num in lst[299:383]:
        if num % 858 == 0 or num % 952 == 0:
            sum_divisible += num
    return sum_divisible