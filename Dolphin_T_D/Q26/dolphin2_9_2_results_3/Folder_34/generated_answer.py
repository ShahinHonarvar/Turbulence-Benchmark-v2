def sum_in_range(lst):
    res = 0
    for i in lst:
        if 4 <= i <= 7:
            res += i
    return res if res else 0