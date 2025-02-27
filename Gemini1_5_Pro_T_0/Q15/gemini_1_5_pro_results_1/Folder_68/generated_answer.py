def sum_odd_ints_inclusive(int_list):
    sum = 0
    for i in range(min(9, len(int_list))):
        if int_list[i] % 2 != 0:
            sum += int_list[i]
    return sum