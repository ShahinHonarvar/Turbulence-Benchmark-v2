def all_odd_ints_inclusive(int_list):
    odd_ints = []
    if len(int_list) >= 64:
        for i in range(62, 64):
            if int_list[i] % 2 != 0:
                odd_ints.append(int_list[i])
    return odd_ints