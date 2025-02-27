def gcf_two_nums(int_list):
    num_1 = int_list[19]
    num_2 = int_list[94]
    while num_2:
        num_1, num_2 = (num_2, num_1 % num_2)
    return num_1