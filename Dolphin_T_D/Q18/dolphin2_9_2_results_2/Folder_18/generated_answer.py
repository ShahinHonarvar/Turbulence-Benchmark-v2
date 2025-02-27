def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for i in range(55, 67):
        if i < len(lst) and (lst[i] % 22 == 0 or lst[i] % 82 == 0):
            sum_ += lst[i]
    return sum_