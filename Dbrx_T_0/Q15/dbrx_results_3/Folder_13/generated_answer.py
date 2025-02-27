def sum_odd_ints_inclusive(lst):
    if len(lst) < 88:
        return 'Input list should have at least 88 elements'
    sum = 0
    for i in range(25, 88):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum