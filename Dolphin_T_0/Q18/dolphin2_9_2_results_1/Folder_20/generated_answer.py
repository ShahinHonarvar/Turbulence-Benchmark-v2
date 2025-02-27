def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for i in range(48, 77):
        if i >= 0 and i < len(lst):
            if lst[i] % -46 == 0 or lst[i] % -82 == 0:
                sum_ += lst[i]
    return sum_