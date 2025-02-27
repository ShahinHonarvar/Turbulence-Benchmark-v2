def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(240, 902):
        if i % 546 == 0 or i % 709 == 0:
            total += i
    return total