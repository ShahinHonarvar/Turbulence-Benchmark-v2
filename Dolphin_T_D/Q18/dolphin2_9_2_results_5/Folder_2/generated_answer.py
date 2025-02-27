def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in lst[73:87]:
        if i % 54 == 0 or i % 82 == 0:
            total += i
    return total