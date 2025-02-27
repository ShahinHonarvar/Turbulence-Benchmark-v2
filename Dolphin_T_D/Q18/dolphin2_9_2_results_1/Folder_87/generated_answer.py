def sum_ints_div_by_either_nums(lst):
    index_start = 18
    index_end = 52
    s = 0
    for i in range(index_start, index_end + 1):
        if lst[i] % 15 == 0 or lst[i] % 57 == 0:
            s += lst[i]
    return s