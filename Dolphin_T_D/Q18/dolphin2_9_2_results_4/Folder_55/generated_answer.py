def sum_ints_div_by_either_nums(lst):
    sum_ = 0
    for i in range(10):
        if i < len(lst):
            if lst[i] % 10 == 0 or lst[i] % 100 == 0:
                sum_ += lst[i]
    return sum_