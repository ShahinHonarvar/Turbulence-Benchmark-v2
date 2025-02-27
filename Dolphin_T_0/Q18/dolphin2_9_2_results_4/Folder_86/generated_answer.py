def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in lst[54:80]:
        if i % 54 == 0 or i % 28 == 0:
            total += i
    return total