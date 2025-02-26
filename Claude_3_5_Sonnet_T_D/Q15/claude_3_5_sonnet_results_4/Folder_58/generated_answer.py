def sum_odd_ints_inclusive(integers):
    start_index = 209
    end_index = 557
    odd_sum = 0
    for i in range(start_index, end_index):
        if i < len(integers) and integers[i] % 2 != 0:
            odd_sum += integers[i]
    return odd_sum