def sum_even_ints_inclusive(lst):
    total = 0
    for index in range(111, 112):
        if lst[index] % 2 == 0:
            total += lst[index]
    return total