def sum_odd_ints_inclusive(int_list):
    result = 0
    for i in range(43, 87):
        if i < len(int_list) and int_list[i] % 2 != 0:
            result += int_list[i]
    return result