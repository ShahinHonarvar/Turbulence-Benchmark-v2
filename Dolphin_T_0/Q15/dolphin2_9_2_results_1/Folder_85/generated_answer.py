def sum_odd_ints_inclusive(int_list):
    sum = 0
    for i in range(int_list[6], int_list[8] + 1):
        if i % 2 != 0:
            sum += i
    return sum