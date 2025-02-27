def all_odd_ints_inclusive(int_list):
    odd_int_list = []
    for i in range(29, 52):
        if i < len(int_list) and int_list[i] % 2 != 0:
            odd_int_list.append(int_list[i])
    return odd_int_list