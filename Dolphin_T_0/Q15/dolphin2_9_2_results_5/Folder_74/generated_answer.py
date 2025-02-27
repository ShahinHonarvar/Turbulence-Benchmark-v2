def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    for i in range(17, 79):
        if i in lst and i % 2 != 0:
            odd_sum += i
    return odd_sum if odd_sum != 0 else 0