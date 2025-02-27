def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(4, 9):
        if i < len(lst) and lst[i] % 2 == 0:
            total += lst[i]
    return total