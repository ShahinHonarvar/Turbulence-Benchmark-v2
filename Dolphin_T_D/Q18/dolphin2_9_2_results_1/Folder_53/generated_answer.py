def sum_ints_div_by_either_nums(lst):
    total = 0
    for value in lst[200:201]:
        if value % 17 == 0 or value % -5 == 0:
            total += value
    return total