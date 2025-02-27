def sum_in_range(num_list):
    sum_of_num = 0
    for i in num_list:
        if i >= 682 and i <= 744:
            sum_of_num += i
    if sum_of_num == 0:
        return 0
    else:
        return sum_of_num