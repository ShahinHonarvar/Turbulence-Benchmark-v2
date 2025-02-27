def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for i in range(527, 539):
        if lst[i] % 2 == 1:
            sum_odd += lst[i]
    return sum_odd if sum_odd != 0 else 0