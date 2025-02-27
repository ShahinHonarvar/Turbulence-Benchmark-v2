def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    if len(lst) > 0 and len(lst) > 2:
        odd_sum += lst[0] if lst[0] % 2 != 0 else 0
        odd_sum += lst[1] if 1 < len(lst) and lst[1] % 2 != 0 else 0
        odd_sum += lst[2] if 2 < len(lst) and lst[2] % 2 != 0 else 0
    return odd_sum