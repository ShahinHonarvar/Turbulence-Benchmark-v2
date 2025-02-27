def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in lst[29:46]:
        if i % 27 == 0 or i % 81 == 0:
            total += i
    return total