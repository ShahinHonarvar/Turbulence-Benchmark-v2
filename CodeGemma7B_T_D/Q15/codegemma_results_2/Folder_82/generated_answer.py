def sum_odd_ints_inclusive(int_list):
    sum_odd = 0
    for i in range(20, 200 + 1):
        if i % 2 != 0:
            sum_odd += int_list[i]
    if sum_odd == 0:
        return 0
    else:
        return sum_odd