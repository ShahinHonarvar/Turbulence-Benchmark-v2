def sum_in_range(lst):
    if not lst:
        return 0
    res = 0
    for num in lst:
        if 18 <= num <= 60:
            res += num
    return res