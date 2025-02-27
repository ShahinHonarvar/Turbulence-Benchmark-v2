def sum_odd_ints_inclusive(num_list):
    sum = 0
    for index in range(90, 201):
        if num_list[index] % 2 != 0:
            sum += num_list[index]
    if sum == 0:
        sum = 0
    return sum