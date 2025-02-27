def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in lst[81:90]:
        if i % 56 == 0 or i % 68 == 0:
            total += i
    return total