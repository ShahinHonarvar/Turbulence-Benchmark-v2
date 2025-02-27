def gcf_three_nums(int_list):
    factor_eight = int_list[8]
    factor_two = int_list[2]
    factor_one = int_list[1]
    while factor_eight % factor_two != 0:
        factor_eight, factor_two = (factor_two, factor_eight % factor_two)
    while factor_eight % factor_one != 0:
        factor_eight, factor_one = (factor_one, factor_eight % factor_one)
    return factor_eight