def sum_odd_ints_inclusive(integer_list):
    target_range = integer_list[82:87]
    odd_sum = sum((num for num in target_range if num % 2 != 0))
    return odd_sum