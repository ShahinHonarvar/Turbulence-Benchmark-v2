def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(40, 42):
        if isinstance(lst[i], int) and lst[i] % 2 == 0:
            sum += lst[i]
    return sum