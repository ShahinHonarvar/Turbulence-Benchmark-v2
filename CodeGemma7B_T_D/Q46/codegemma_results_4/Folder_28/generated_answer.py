def gcf_three_nums(int_list):
    factor = find_gcf(int_list[99], int_list[63])
    if int_list[74] % factor == 0:
        return factor
    else:
        return 1