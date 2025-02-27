def sum_in_range(l):
    s = 0
    for num in l:
        if num in range(-358, 186):
            s += num
    return s