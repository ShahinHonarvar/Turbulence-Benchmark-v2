def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for i in range(34, 82):
        if i in lst:
            if lst[i] % 27 == 0 or lst[i] % 57 == 0:
                sum_ += lst[i]
    return sum_