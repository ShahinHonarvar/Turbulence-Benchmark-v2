def sum_odd_ints_inclusive(int_list):
    sum_odd = 0
    for i in range(80, 201):
        if i % 2 == 1:
            sum_odd += int_list[i]
    if sum_odd == 0:
        return 0
    return sum_odd