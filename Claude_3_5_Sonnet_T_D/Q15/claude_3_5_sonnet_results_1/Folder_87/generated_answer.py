def sum_odd_ints_inclusive(integers):
    start_index = 36
    end_index = 47
    odd_sum = 0
    if len(integers) < end_index:
        end_index = len(integers)
    for i in range(start_index, end_index):
        if integers[i] % 2 != 0:
            odd_sum += integers[i]
    return odd_sum