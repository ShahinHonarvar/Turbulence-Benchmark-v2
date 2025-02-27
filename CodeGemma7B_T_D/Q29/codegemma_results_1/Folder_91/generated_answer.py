def gcf_two_nums(num_list):
    num_list_len = len(num_list)
    common_factors = []
    for x in range(1, num_list_num_list_len + 1):
        if num_list_len % x == 0 and num_list_num_list_len % x == 0:
            common_factors.append(x)
    return common_factors[-1]