def sum_in_range(lst):
    res = 0
    for x in lst:
        if 20 <= x <= 93:
            res += x
    return res