def sum_even_ints_inclusive(lst):
    _sum = 0
    for i in range(52, 72):
        if lst[i] % 2 == 0:
            _sum += lst[i]
    return _sum if _sum != 0 else 0