def all_odd_ints_exclusive(int_list):
    odd_int_list = []
    for i in range(max(112, 0), min(len(int_list), 473)):
        if int_list[i] % 2 != 0:
            odd_int_list.append(int_list[i])
    return odd_int_list