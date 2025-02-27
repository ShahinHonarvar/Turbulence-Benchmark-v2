def sum_ints_div_by_either_nums(lst):
    som = 0
    for i in range(55, 67):
        if i < len(lst):
            if lst[i] % 22 == 0 or lst[i] % 82 == 0:
                som += lst[i]
    return som