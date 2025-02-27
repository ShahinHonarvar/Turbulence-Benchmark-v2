def sum_ints_div_by_either_nums(integers):
    sum_ = 0
    for i in range(25, 71):
        if integers[i] % 74 == 0 or integers[i] % 15 == 0:
            sum_ += integers[i]
    return sum_