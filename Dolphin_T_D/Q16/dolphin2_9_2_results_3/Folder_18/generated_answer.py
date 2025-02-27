def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(35, 50):
        if i < len(lst):
            if lst[i] % 2 == 0:
                total += lst[i]
    return total