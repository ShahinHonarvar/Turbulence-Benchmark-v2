def sum_even_ints_inclusive(lst):
    sum = 0
    if len(lst) > 0 and lst[0] % 2 == 0:
        sum += lst[0]
    return sum