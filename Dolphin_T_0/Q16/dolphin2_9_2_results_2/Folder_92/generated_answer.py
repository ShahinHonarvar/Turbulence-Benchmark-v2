def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(len(lst)):
        if 0 <= i <= 1 and lst[i] % 2 == 0:
            total += lst[i]
    return total