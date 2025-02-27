def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(281, 695):
        if int_list[i] % -722 == 0 or int_list[i] % -731 == 0:
            sum += int_list[i]
    return sum