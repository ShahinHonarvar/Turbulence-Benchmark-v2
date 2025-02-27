def sum_odd_ints_inclusive(lst):
    if len(lst) < 200:
        return 'Input list should have at least 200 elements'
    sum = 0
    for i in range(70, 201):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum