def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[55:85]:
        if num % -24 == 0 or num % -11 == 0:
            total += num
    return total