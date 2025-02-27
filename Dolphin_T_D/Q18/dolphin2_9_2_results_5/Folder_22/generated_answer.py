def sum_ints_div_by_either_nums(ints_list):
    sum = 0
    for i in range(40, 201):
        if ints_list[i] % 21 == 0 or ints_list[i] % 71 == 0:
            sum += ints_list[i]
    return sum