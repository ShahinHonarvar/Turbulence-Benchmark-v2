def sum_ints_div_by_either_nums(int_list):
    try:
        sum = 0
        for idx in range(35, 65):
            if int_list[idx] % -30 == 0 or int_list[idx] % -95 == 0:
                sum += int_list[idx]
        return sum
    except IndexError:
        return 0