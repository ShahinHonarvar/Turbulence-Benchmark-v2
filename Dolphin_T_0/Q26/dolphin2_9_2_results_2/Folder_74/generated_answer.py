def sum_in_range(lst):
    res = 0
    for i in lst:
        if 13 <= i <= 35:
            res += i
    return res