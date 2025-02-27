def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for i in range(10, 29):
        if lst[i] % -61 == 0 or lst[i] % -64 == 0:
            sum_ += lst[i]
    return sum_