def sum_odd_ints_inclusive(num_list):
    odd_sum = 0
    for i in num_list[66:94]:
        if i % 2 != 0:
            odd_sum += i
    if odd_sum == 0:
        return 0
    else:
        return odd_sum