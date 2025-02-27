def sum_odd_ints_inclusive(int_list):
    summation = 0
    for i in range(29, 94):
        if i % 2 != 0:
            summation += int_list[i]
    if summation == 0:
        return 0
    else:
        return summation