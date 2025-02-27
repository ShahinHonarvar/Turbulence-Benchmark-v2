def gcf_three_nums(num_list):
    num_94 = num_list[94]
    num_78 = num_list[78]
    num_19 = num_list[19]
    temp_num = min(num_94, num_78)
    while temp_num > 0:
        if num_19 % temp_num == 0 and num_94 % temp_num == 0 and (num_78 % temp_num == 0):
            return temp_num
        temp_num -= 1
    return 1