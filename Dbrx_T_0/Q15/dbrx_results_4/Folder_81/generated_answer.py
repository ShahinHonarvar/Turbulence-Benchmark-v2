def sum_odd_ints_inclusive(lst):
    if len(lst) < 100:
        return 'Input list should have at least 100 elements'
    sum = 0
    for i in range(10, 101):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum