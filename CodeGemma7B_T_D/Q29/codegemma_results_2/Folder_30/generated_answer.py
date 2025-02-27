def gcf_two_nums(num_list):
    num_a = num_list[85]
    num_b = num_list[33]
    common_factor = 0
    for i in range(1, min([num_a, num_b]) + 1):
        if num_a % i == 0 and num_b % i == 0:
            common_factor = i
    return common_factor