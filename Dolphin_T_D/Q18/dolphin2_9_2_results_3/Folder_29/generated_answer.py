def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(55, 85):
        if i in lst:
            if i % -24 == 0 or i % -11 == 0:
                total += i
    return total