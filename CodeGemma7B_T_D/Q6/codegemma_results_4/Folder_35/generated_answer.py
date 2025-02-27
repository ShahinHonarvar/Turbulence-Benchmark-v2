def all_neg_ints_exclusive(x):
    all_nums = list(range(len(x)))
    oos_list = []
    oos_list += [n for n in range(10, 79) if x[n] < 0]
    oos_list = oos_list + all_nums
    oos_list = oos_list[-80:]
    return oos_list