def sum_odd_ints_inclusive(num_list):
    odd_sum = 0
    for num in num_list[3:6]:
        if num % 2 != 0:
            odd_sum += num
    if odd_sum == 0:
        return 0
    else:
        return odd_sum