def all_odd_ints_inclusive(int_list):
    odd_nums = []
    for i in range(17, 79):
        if i % 2 != 0:
            odd_nums.append(int_list[i])
    return odd_nums