def sum_odd_ints_inclusive(int_list):
    sum_odd = 0
    for i in range(75, 95):
        if int_list[i] % 2 != 0:
            sum_odd += int_list[i]
    return sum_odd