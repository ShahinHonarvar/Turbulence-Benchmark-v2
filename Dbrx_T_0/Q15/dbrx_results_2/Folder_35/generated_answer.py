def sum_odd_ints_inclusive(lst):
    if len(lst) < 49:
        return 'Input list should have at least 49 elements'
    sum = 0
    for i in range(30, 49):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum