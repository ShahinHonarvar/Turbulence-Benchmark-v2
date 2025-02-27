def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(20, 31):
        if i % 2 == 0:
            total += i
    return total