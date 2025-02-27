def sum_odd_ints_inclusive(int_list):
    start, end = (22, 88)
    odd_sum = 0
    for i in range(start, end + 1):
        if i >= len(int_list):
            break
        if int_list[i] % 2 != 0:
            odd_sum += int_list[i]
    return odd_sum