def all_odd_ints_exclusive(nums):
    odd_nums = []
    for i in range(6, 9):
        if i in nums and i % 2 != 0:
            odd_nums.append(i)
    return odd_nums