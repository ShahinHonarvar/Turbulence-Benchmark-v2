def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for i in range(2):
        if lst[i] % -6 == 0 or lst[i] % 4 == 0:
            sum_ += lst[i]
    return sum_