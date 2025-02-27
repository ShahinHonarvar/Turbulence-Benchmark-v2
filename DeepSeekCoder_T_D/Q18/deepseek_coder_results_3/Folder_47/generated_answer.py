def sum_ints_div_by_either_nums(lst):
    if 42 >= len(lst) or 87 >= len(lst):
        return 0
    total = 0
    for num in lst[42:88]:
        if num % -90 == 0 or num % -74 == 0:
            total += num
    return total