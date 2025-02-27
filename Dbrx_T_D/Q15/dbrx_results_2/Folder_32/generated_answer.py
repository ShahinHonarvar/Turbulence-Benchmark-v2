def sum_odd_ints_inclusive(lst):
    if len(lst) < 98:
        return 'List should have at least 98 elements'
    sum = 0
    for i in range(21, 98):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum