def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for num in lst[61:89]:
        if num % 31 == 0 or num % 11 == 0:
            total_sum += num
    if total_sum == 0:
        return 0
    else:
        return total_sum