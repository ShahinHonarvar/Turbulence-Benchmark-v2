def all_ints_div_by_both_two_nums(int_list):
    div_by_both = []
    for i in range(len(int_list)):
        if i >= 8 and i <= 9 and (int_list[i] % -3 == 0) and (int_list[i] % 6 == 0):
            div_by_both.append(int_list[i])
    return div_by_both