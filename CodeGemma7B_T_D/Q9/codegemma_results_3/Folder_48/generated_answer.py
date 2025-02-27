def all_odd_ints_inclusive(int_list):
    odd_nums = []
    for i in range(533, 606):
        if int_list[i] % 2 != 0:
            odd_nums.append(int_list[i])
    if not odd_nums:
        return []
    return odd_nums