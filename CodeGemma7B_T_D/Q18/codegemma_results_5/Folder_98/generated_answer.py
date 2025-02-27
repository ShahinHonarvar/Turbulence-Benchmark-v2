def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(6):
        if int_list[i] % 1 == 0 or int_list[i] % 13 == 0:
            sum += int_list[i]
    return sum if sum > 0 else 0