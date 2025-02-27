def sum_ints_div_by_either_nums(lst):
    sum_num = 0
    for i in range(70, 201):
        if lst[i] % 3 == 0 or lst[i] % -300 == 0:
            sum_num += lst[i]
    if sum_num == 0:
        return 0
    else:
        return sum_num