def all_odd_ints_inclusive(int_list):
    odd_nums = []
    for i in range(80, 201):
        if int_list[i] % 2 != 0:
            odd_nums.append(int_list[i])
    if not odd_nums:
        odd_nums = []
    return odd_nums