def sum_odd_ints_inclusive(num_list):
    sum = 0
    for i in range(len(num_list)):
        if i >= 75 and i <= 88:
            if num_list[i] % 2 != 0:
                sum += num_list[i]
    return sum