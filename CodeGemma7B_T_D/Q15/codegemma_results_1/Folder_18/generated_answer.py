def sum_odd_ints_inclusive(num_list):
    sum = 0
    for i in range(35, 50):
        if num_list[i] % 2 != 0:
            sum += num_list[i]
    if sum == 0:
        return 0
    else:
        return sum