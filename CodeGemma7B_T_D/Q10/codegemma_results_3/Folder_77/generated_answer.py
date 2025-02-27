def all_odd_ints_exclusive(int_list):
    temp_list = []
    for i in range(111, 473):
        if int_list[i] % 2 != 0:
            temp_list.append(int_list[i])
    return temp_list