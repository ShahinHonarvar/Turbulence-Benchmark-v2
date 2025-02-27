def sum_odd_ints_inclusive(num_list):
    sum = 0
    for i in range(14, 65):
        if i >= len(num_list):
            break
        if num_list[i] % 2 != 0:
            sum += num_list[i]
    return sum