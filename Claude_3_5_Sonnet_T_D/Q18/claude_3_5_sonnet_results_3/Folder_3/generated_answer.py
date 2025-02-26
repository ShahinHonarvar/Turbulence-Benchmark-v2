def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(38, 53):
        if i < len(int_list):
            if int_list[i] % -41 == 0 or int_list[i] % -47 == 0:
                total += int_list[i]
    return total