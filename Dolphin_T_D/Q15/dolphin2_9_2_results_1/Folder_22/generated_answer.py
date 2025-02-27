def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    indices = range(40, 42)
    for i in indices:
        if lst[i] % 2 != 0:
            odd_sum += lst[i]
    return odd_sum if odd_sum != 0 else 0