def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(1, 6):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total if total != 0 else 'No even integers exist in the specified range'