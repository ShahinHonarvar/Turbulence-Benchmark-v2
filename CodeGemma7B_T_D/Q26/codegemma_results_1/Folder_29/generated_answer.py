def sum_in_range(lst):
    tot = 0
    for num in lst:
        if 18 <= num <= 60:
            tot += num
    return tot