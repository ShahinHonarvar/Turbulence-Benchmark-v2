def sum_ints_div_by_either_nums(my_list):
    sum = 0
    for i in range(58, 76):
        temp = my_list[i]
        if temp % 72 == 0 and temp % 62 == 0:
            sum += temp
    return sum