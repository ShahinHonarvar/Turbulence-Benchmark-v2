def all_odd_ints_inclusive(int_list):
    odd_int_list = []
    for idx in range(17, 79):
        if idx % 2 != 0:
            odd_int_list.append(int_list[idx])
    return odd_int_list