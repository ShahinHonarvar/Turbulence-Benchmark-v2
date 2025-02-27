def sum_even_ints_inclusive(lst):
    if len(lst) < 49:
        return 'List is too short.'
    sum = 0
    for i in range(30, 49):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum