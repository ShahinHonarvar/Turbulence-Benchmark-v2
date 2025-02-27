def sum_ints_div_by_either_nums(lst):
    if len(lst) < 2:
        return 0
    total = 0
    for num in lst[0:2]:
        if num % 6 == 0 or num % 4 == 0:
            total += num
    return total