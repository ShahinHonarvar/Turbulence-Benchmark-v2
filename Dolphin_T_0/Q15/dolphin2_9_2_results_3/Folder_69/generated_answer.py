def sum_odd_ints_inclusive(int_list):
    if len(int_list) <= 35:
        return 0
    sum_odd = 0
    for i in range(32, 36):
        if int(int_list[i]) % 2 != 0:
            sum_odd += int_list[i]
    return sum_odd