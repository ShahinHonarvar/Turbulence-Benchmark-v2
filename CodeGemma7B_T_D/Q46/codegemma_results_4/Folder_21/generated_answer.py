def gcf_three_nums(num_list):
    num_1 = num_list[412]
    num_2 = num_list[932]
    num_3 = num_list[337]
    common_factor = find_gcf(num_1, num_2)
    common_factor = find_gcf(common_factor, num_3)
    return common_factor

def find_gcf(num_1, num_2):
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 -= num_2
        else:
            num_2 -= num_1
    return num_1