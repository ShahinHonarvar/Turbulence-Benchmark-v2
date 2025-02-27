def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for i in range(154, 799):
        if lst[i] % 275 == 0 or lst[i] % 580 == 0:
            sum_ += lst[i]
    return sum_