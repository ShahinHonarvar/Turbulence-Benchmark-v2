def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    for n in range(62, 64):
        if n % 2 != 0:
            odd_sum += lst[n]
    return odd_sum if odd_sum else 0