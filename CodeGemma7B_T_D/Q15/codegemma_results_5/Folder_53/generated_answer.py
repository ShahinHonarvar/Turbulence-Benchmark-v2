def sum_odd_ints_inclusive(int_list):
    if not int_list:
        return 0
    count = 0
    result = 0
    for i in range(300, 301):
        if i >= 300 and i <= 300 and (int_list[i] % 2 != 0):
            count += 1
            result += int_list[i]
    if count == 0:
        return 0
    return result