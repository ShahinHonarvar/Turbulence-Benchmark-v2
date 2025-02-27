def sum_in_range(lst):
    res = 0
    for i in lst:
        if -100 <= i <= -55:
            res += i
    return res if res != 0 else 0