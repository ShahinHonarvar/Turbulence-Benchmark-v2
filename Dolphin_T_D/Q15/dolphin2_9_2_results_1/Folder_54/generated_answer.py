def sum_odd_ints_inclusive(lst):
    total = sum((lst[i] for i in range(34, 56) if lst[i] % 2 != 0))
    return total if total else 0