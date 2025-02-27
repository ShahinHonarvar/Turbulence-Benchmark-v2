def all_odd_ints_exclusive(nums):
    odd_nums = []
    for i in range(30, 200):
        if i % 2 != 0:
            odd_nums.append(i)
    return odd_nums if odd_nums else []