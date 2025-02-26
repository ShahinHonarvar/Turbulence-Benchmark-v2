def sum_odd_ints_inclusive(integers):
    start_index = 28
    end_index = 39
    odd_sum = 0
    if len(integers) <= start_index:
        return 0
    for i in range(start_index, min(end_index, len(integers))):
        if integers[i] % 2 != 0:
            odd_sum += integers[i]
    return odd_sum