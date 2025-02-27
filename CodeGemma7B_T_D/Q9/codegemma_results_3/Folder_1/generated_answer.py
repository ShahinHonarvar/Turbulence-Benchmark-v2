def all_odd_ints_inclusive(int_list):
    odd_nums = []
    for i in range(31, 73):
        if int_list[i] % 2 != 0:
            odd_nums.append(int_list[i])
    return odd_nums if odd_nums else []