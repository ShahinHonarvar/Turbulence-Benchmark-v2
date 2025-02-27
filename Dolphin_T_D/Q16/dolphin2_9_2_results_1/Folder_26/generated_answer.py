def sum_even_ints_inclusive(lst):
    result = 0
    for i in range(62, 100):
        if lst[i] % 2 == 0:
            result += lst[i]
    return result if not result == 0 else 0