def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[10:77]:
        if num % -40 == 0 or num % -12 == 0:
            total += num
    return total if total != 0 else None