def sum_ints_div_by_either_nums(ints):
    sum_ = 0
    for i in range(10):
        if ints[i] % 6 == 0 or ints[i] % -3 == 0:
            sum_ += ints[i]
    return sum_