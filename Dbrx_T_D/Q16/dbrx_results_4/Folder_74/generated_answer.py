def sum_even_ints_inclusive(lst):
    if len(lst) < 79:
        return 0
    sum = 0
    for i in range(17, 79):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum