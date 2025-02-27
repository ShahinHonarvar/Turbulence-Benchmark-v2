def all_odd_ints_inclusive(int_list):
    if int_list[29] % 2 == 0 or int_list[51] % 2 == 0:
        return []
    odd_nums = []
    for i in range(29, 52):
        if int_list[i] % 2 != 0:
            odd_nums.append(int_list[i])
    return odd_nums