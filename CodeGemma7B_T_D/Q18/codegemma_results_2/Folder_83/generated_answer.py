def sum_ints_div_by_either_nums(list):
    sum = 0
    for i in range(90, 201):
        if list[i] % 31 == 0 or list[i] % 13 == 0:
            sum += list[i]
    return sum