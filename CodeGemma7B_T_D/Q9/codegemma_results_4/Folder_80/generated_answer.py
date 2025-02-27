def all_odd_ints_inclusive(num_list):
    odd_nums = []
    for i in range(64, 66):
        if num_list[i] % 2 != 0:
            odd_nums.append(num_list[i])
    return odd_nums