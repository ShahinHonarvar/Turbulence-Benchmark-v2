def sum_even_ints_inclusive(lst):
    if len(lst) < 88:
        return 0
    return sum((lst[i] for i in range(30, 88) if lst[i] % 2 == 0))