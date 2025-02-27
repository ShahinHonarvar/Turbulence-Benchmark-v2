def gcf_three_nums(num_list):
    num_one = num_list[7]
    num_two = num_list[9]
    num_three = num_list[0]
    common_factor = 1
    for factor in range(1, min([num_one, num_two, num_three]) + 1):
        if num_one % factor == 0 and num_two % factor == 0 and (num_three % factor == 0):
            common_factor = factor
    return common_factor