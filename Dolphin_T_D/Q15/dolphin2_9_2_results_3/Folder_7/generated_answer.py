def sum_odd_ints_inclusive(int_list):
    sum_odd_ints = 0
    for i in range(661, 925):
        if int_list[i] % 2 != 0:
            sum_odd_ints += int_list[i]
    return sum_odd_ints