def sum_odd_ints_inclusive(l):
    od_sum = 0
    for i in range(27, 56):
        if l[i] % 2 == 1:
            od_sum += l[i]
    return od_sum