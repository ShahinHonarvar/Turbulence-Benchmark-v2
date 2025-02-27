def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(78, 82):
        if i in range(len(int_list)):
            if int_list[i] % 76 == 0 or int_list[i] % 60 == 0:
                total += int_list[i]
    return total