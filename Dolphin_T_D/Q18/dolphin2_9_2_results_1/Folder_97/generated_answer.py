def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(58, 76):
        if int_list[i] % 72 == 0 or int_list[i] % 62 == 0:
            sum += int_list[i]
    return sum if sum != 0 else 0