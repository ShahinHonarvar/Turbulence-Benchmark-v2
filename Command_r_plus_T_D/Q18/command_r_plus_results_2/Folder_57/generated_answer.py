def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for i in range(51, 77):
        if lst[i] % -90 == 0 or lst[i] % -59 == 0:
            sum_ += lst[i]
    return sum_