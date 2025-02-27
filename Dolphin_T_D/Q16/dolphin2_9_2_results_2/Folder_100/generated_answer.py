def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(min(42, len(lst)), min(69, len(lst))):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total if total != 0 else 0