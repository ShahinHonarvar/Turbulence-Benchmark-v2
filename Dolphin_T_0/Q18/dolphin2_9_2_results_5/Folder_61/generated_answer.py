def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in lst[:7]:
        if i % -5 == 0 or i % -6 == 0:
            total += i
    return total