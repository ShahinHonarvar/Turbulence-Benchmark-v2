def sum_odd_ints_inclusive(lst):
    sum_odd_ints = 0
    for i in range(56, 99):
        if i in lst:
            sum_odd_ints += i
    return sum_odd_ints