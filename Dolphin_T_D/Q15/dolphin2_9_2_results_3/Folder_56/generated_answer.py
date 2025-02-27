def sum_odd_ints_inclusive(int_list):
    result = 0
    for i in range(int_list[0], int_list[0] + 1):
        if i % 2 != 0:
            result += i
    if result == 0:
        return 0
    else:
        return result