def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in lst[:4]:
        if i % 11 == 0 or i % -7 == 0:
            total += i
    return total