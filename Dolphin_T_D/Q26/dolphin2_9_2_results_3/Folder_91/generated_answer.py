def sum_in_range(lst):
    res = 0
    for num in lst:
        if -8 <= num <= 8:
            res += num
    return res