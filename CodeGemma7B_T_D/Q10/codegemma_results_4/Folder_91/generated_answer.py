def all_odd_ints_exclusive(int_list):
    odd_nums = []
    for i in range(6):
        if i % 2 != 0:
            odd_nums.append(i)
    return odd_nums