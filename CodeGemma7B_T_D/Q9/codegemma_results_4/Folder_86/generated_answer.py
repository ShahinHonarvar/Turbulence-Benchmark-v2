def all_odd_ints_inclusive(int_list):
    odd_list = []
    for i in range(31, 35):
        if int_list[i] % 2 != 0:
            odd_list.append(int_list[i])
    return odd_list