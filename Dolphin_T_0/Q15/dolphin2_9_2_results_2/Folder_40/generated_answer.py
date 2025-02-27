def sum_odd_ints_inclusive(l):
    sum_val = 0
    for i in range(3):
        if l[i] % 2 != 0:
            sum_val += l[i]
    return sum_val