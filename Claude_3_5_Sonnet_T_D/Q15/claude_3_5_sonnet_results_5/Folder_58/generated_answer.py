def sum_odd_ints_inclusive(integers):
    start_index = 209
    end_index = 556
    if len(integers) <= start_index:
        return 0
    end_index = min(end_index, len(integers) - 1)
    odd_sum = sum((num for num in integers[start_index:end_index + 1] if num % 2 != 0))
    return odd_sum