def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(533, 606):
        if i < len(lst):
            total += lst[i] if lst[i] % 2 == 0 else 0
    return total