def sum_odd_ints_inclusive(int_list):
    result = 0
    for i in range(66, 94):
        if int_list[i] % 2 != 0:
            result += int_list[i]
    return result