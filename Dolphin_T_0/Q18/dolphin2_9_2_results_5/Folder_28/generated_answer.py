def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[34:81 + 1]:
        if num % 27 == 0 or num % 57 == 0:
            total += num
    if total == 0:
        return 0
    else:
        return total