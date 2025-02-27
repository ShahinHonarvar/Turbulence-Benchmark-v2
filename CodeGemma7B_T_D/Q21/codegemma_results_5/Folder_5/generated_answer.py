def all_ints_div_by_num(int_list):
    new_list = []
    for i in range(1, 5):
        if int_list[i % len(int_list)] % -6 == 0:
            new_list.append(int_list[i % len(int_list)])
    return new_list