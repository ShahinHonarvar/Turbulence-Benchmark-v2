def sum_odd_ints_inclusive(integers):
    target_range = integers[82:87]
    odd_sum = sum((num for num in target_range if num % 2 != 0))
    return odd_sum