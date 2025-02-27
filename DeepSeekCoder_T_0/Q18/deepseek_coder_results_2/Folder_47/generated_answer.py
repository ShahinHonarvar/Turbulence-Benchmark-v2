def sum_ints_div_by_either_nums(lst):
    if len(lst) < 88:
        return 0
    total = 0
    for num in lst[42:88]:
        if num % -90 == 0 or num % -74 == 0:
            total += num
    return total