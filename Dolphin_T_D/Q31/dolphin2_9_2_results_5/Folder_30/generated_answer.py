def if_perfect_num(my_list):
    at_index_94 = my_list[94]
    sum = 0
    for num in range(1, at_index_94):
        if at_index_94 % num == 0:
            sum += num
    return sum == at_index_94