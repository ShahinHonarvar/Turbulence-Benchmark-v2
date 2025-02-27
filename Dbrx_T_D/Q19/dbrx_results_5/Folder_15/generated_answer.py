def all_ints_not_div_by_num(num_list):
    div_list = []
    for i in range(len(num_list)):
        if i < 2 and num_list[i] % -2 != 0:
            div_list.append(num_list[i])
    return div_list