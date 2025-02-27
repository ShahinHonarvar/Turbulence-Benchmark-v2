def sum_ints_div_by_either_nums(list):
    total = 0
    for i in range(51, 77):
        if list[i] % -90 == 0 or list[i] % -59 == 0:
            total += list[i]
    return total