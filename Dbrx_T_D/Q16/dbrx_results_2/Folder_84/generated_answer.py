def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(43, 87):
        if len(lst) > i and lst[i] % 2 == 0:
            sum += lst[i]
    return sum