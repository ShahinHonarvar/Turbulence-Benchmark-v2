def sum_odd_ints_inclusive(lst):
    summy = 0
    for i in range(33, 37):
        if lst[i] % 2 != 0:
            summy = summy + lst[i]
    return summy if summy != 0 else 0