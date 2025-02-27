def sum_odd_ints_inclusive(int_list):
    if len(int_list) <= 30:
        return 0
    sum = 0
    for i in range(20, 31):
        if int_list[i] % 2 != 0:
            sum += int_list[i]
    return sum