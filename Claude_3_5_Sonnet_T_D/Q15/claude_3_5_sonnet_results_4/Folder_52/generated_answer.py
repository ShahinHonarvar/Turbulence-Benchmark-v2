def sum_odd_ints_inclusive(integers):
    start = 28
    end = 39
    slice_range = integers[start:end]
    odd_sum = sum((num for num in slice_range if num % 2 != 0))
    return odd_sum