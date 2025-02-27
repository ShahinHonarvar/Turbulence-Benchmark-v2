def sum_in_range(numxs):
    s = 0
    for numx in numxs:
        if 2 <= numx <= 9:
            s += numx
    return s