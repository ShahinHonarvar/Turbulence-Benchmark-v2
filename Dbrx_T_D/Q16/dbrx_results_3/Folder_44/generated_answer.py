def sum_even_ints_inclusive(lst):
    if len(lst) < 69:
        return 0
    sum = 0
    for i in range(13, 69):
        if i < len(lst) and lst[i] % 2 == 0:
            sum += lst[i]
    return sum