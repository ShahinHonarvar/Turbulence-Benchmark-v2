def sum_odd_ints_inclusive(num_list):
    sum_odd = 0
    for i in range(13, 68):
        if num_list[i] % 2 != 0:
            sum_odd += num_list[i]
    if sum_odd == 0:
        return 0
    return sum_odd