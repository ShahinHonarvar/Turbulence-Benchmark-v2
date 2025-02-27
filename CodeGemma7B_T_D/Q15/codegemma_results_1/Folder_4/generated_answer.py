def sum_odd_ints_inclusive(my_list):
    sum = 0
    for i in range(12, 93):
        if i % 2 != 0:
            sum += my_list[i]
    if sum == 0:
        return 0
    else:
        return sum