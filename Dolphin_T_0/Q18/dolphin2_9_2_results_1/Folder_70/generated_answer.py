def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in lst[42:44]:
        if i % 15 == 0 or i % 87 == 0:
            total += i
    return total