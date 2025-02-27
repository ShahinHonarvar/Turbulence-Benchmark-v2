def sum_odd_ints_inclusive(lst):
    odd_ints_sum = 0
    for i in range(209, 567):
        if lst[i] % 2 != 0:
            odd_ints_sum += lst[i]
    return odd_ints_sum if odd_ints_sum != 0 else 0