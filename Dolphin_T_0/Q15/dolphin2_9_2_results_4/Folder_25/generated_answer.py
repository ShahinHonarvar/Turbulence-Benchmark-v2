def sum_odd_ints_inclusive(lst):
    odd_sum = sum((num for num in lst[29:94] if num % 2 != 0))
    if odd_sum != 0:
        return odd_sum
    else:
        return 0