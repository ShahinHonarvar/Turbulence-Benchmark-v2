def sum_odd_ints_inclusive(int_list):
    sum = 0
    for i in range(0, 3, 1):
        if i > len(int_list) - 1:
            break
        if int_list[i] % 2 != 0:
            sum += int_list[i]
    return sum