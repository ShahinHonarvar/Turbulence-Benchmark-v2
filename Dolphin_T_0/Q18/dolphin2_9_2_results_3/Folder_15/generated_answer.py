def sum_ints_div_by_either_nums(ints_list):
    sum = 0
    for i in range(3):
        if ints_list[i] % -2 == 0 or ints_list[i] % 3 == 0:
            sum += ints_list[i]
    return sum