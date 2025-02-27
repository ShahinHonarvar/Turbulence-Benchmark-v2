def sum_in_range(lst):
    s = 0
    for i in lst:
        if -64 <= i <= 42:
            s += i
    return s