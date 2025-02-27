def all_odd_ints_exclusive(int_list):
    odd_int_list = []
    for i in range(1, 2):
        if i < len(int_list) and int_list[i] % 2 != 0:
            odd_int_list.append(int_list[i])
    return odd_int_list