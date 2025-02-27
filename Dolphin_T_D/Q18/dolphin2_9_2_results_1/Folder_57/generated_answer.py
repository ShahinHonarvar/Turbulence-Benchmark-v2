def sum_ints_div_by_either_nums(ints):
    total = 0
    for num in ints[51:77]:
        if num % -90 == 0 or num % -59 == 0:
            total += num
    return total