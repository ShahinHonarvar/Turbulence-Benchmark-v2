def sum_odd_ints_inclusive(lst):
    odd_sum = sum((i for i in lst[0:1] if i % 2 != 0))
    return odd_sum