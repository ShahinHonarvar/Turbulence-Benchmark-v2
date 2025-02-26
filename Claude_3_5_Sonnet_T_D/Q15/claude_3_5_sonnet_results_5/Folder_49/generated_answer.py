def sum_odd_ints_inclusive(integers):
    start = 80
    end = 201
    valid_range = integers[start:end]
    odd_sum = sum((num for num in valid_range if num % 2 != 0))
    return odd_sum