def all_ints_div_by_both_two_nums(int_list):
    div_by_both = []
    for i in range(86, 90):
        if i < len(int_list):
            if int_list[i] % -61 == 0 and int_list[i] % -79 == 0:
                div_by_both.append(int_list[i])
    return div_by_both