def gcf_three_nums(num_list):
    num_15 = num_list[15]
    num_51 = num_list[51]
    num_76 = num_list[76]
    while num_15 != num_51:
        if num_15 < num_51:
            num_15 += num_76
        elif num_15 > num_51:
            num_51 += num_15
    return num_15