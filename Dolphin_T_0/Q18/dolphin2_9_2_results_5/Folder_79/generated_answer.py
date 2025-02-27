def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in ints[8:10]:
        if i % -3 == 0 or i % 6 == 0:
            total += i
    return total