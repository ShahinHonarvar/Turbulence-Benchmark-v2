def sum_ints_div_by_either_nums(list_):
    total = 0
    for i in range(24, 33):
        if list_[i] % 35 == 0 or list_[i] % 87 == 0:
            total += list_[i]
    return total