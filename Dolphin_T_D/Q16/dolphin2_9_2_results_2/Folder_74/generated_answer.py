def sum_even_ints_inclusive(lst):
    if not lst:
        return 0
    sum = 0
    for i in range(17, 79):
        if i < len(lst):
            if lst[i] % 2 == 0:
                sum += lst[i]
    return sum