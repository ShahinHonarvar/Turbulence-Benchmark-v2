def sum_odd_ints_inclusive(num_list):
    sum_odd = 0
    for i in range(32, 36):
        if num_list[i] % 2 != 0:
            sum_odd += num_list[i]
    return sum_odd or 0