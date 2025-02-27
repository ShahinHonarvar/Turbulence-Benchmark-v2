def sum_odd_ints_inclusive(int_list):
    sum = 0
    for i in range(max(30, len(int_list) - 1), 199, -1):
        if int_list[i] % 2 != 0:
            sum += int_list[i]
    return sum