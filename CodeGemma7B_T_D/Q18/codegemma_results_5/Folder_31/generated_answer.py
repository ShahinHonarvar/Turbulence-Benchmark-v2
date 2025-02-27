def sum_ints_div_by_either_nums(int_list):
    if not int_list or len(int_list) < 89:
        return 0
    sum = 0
    for i in range(56, 89 + 1):
        if int_list[i] % 59 == 0 or int_list[i] % 79 == 0:
            sum += int_list[i]
    if sum == 0:
        return 0
    return sum