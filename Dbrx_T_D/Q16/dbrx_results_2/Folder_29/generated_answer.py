def sum_even_ints_inclusive(lst):
    if len(lst) < 97:
        return 'Input list should have at least 97 elements'
    sum = 0
    for i in range(59, 98):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum