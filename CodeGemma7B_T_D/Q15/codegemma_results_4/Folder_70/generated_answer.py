def sum_odd_ints_inclusive(int_list):
    sum_of_odd_ints = 0
    for i in range(28, 33):
        if int_list[i] % 2 != 0:
            sum_of_odd_ints += int_list[i]
    if sum_of_odd_ints == 0:
        return 0
    else:
        return sum_of_odd_ints