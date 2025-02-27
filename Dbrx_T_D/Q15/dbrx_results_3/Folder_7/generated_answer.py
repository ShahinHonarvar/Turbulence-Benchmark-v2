def sum_odd_ints_inclusive(num_list):
    sum = 0
    for i in range(661, 925):
        if i < len(num_list) and num_list[i] % 2 != 0:
            sum += num_list[i]
    return sum