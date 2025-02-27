def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(26, 53):
        if i < len(lst) and lst[i] % 2 == 0:
            total += lst[i]
    return total