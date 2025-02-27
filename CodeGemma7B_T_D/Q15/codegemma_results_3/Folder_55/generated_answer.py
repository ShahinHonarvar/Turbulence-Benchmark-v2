def sum_odd_ints_inclusive(int_list):
    sum = 0
    for i in range(len(int_list)):
        if i in range(0, 11) and int_list[i] % 2 != 0:
            sum += int_list[i]
    if sum == 0:
        return 0
    else:
        return sum