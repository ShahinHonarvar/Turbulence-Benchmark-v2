def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[50:93]:
        if num % -94 == 0 or num % -95 == 0:
            total += num
    return total