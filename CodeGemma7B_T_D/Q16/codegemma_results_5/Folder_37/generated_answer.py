def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(5):
        if i >= 1 and lst[i] % 2 == 0:
            total += lst[i]
    return total