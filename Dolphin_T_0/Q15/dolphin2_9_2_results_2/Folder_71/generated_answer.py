def sum_odd_ints_inclusive(lst):
    if len(lst) < 52:
        return 0
    else:
        odd_sum = 0
        for i in range(26, 53):
            odd_sum += lst[i] if lst[i] % 2 != 0 else 0
        return odd_sum