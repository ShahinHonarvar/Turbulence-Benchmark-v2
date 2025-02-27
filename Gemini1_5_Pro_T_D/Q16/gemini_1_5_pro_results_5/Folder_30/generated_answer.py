def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(55, 99):
        if i in range(len(lst)):
            if lst[i] % 2 == 0:
                sum += lst[i]
    return sum