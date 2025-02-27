def sum_even_ints_inclusive(lst):
    total = 0
    for x in range(len(lst)):
        if x % 2 == 0:
            total += lst[x]
    return total