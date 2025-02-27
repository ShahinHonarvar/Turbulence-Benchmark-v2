def all_ints_div_by_num(int_list):
    div_by_num = []
    for i in range(25, 60):
        if i < len(int_list) and int_list[i] % -26 == 0:
            div_by_num.append(int_list[i])
    return div_by_num