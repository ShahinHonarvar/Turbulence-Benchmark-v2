def sum_odd_ints_inclusive(num_list):
    sum_odd_ints = 0
    for index in range(34, 56):
        if index % 2 != 0:
            sum_odd_ints += num_list[index]
    if sum_odd_ints == 0:
        return 0
    else:
        return sum_odd_ints