def all_odd_ints_exclusive(num_list):
    odd_nums = []
    for i in range(1, 8):
        if i % 2 != 0:
            odd_nums.append(i)
    return odd_nums