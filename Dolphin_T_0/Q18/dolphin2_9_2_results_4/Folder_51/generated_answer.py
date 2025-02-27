def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in lst[6:10]:
        if i % -1 == 0 or i % -10 == 0:
            total += i
    return total