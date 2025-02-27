def all_ints_div_by_num(num_list):
    int_list_div_by_num = []
    for number in num_list:
        if number / 3 == int(number / 3):
            int_list_div_by_num.append(number)
    return int_list_div_by_num