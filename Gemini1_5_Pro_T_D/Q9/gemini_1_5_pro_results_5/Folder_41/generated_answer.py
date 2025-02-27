def all_odd_ints_inclusive(int_list):
    new_list = []
    if len(int_list) > 6:
        if int_list[6] % 2 != 0:
            new_list.append(int_list[6])
    return new_list