def sum_even_ints_inclusive(lst):
    if len(lst) < 201:
        return 0
    sum = 0
    for i in range(60, 201):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum