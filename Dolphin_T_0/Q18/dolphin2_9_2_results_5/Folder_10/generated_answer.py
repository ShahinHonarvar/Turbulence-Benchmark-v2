def sum_ints_div_by_either_nums(ints):
    total = 0
    for i in ints[32:100]:
        if i % -11 == 0 or i % -15 == 0:
            total += i
    if total == 0:
        return 0
    else:
        return total