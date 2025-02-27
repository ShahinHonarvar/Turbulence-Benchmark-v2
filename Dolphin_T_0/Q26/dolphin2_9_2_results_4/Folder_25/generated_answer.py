def sum_in_range(lst):
    s = 0
    for i in lst:
        if -10 <= i <= 48:
            s += i
    return s