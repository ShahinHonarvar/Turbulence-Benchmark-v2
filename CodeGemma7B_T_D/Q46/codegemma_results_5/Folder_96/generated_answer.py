def gcf_three_nums(num_list):
    num_29 = num_list[29]
    num_74 = num_list[74]
    num_49 = num_list[49]
    while num_29 != num_74:
        if num_29 < num_74:
            num_29 += num_49
        else:
            num_74 += num_49
    return num_29