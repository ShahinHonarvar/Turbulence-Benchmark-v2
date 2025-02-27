def gcf_three_nums(num_list):
    num_one = num_list[41]
    num_two = num_list[69]
    num_three = num_list[28]
    factor = 1
    for i in range(1, min(num_one, num_two, num_three) + 1):
        if num_one % i == 0 and num_two % i == 0 and (num_three % i == 0):
            factor = i
    return factor