def all_odd_ints_inclusive(int_list):
    new_list = []
    if int_list:
        if int_list[0] % 2 != 0:
            new_list.append(int_list[0])
    return new_list