def all_odd_ints_inclusive(nums):
    odd_nums = []
    for i in range(29, 94):
        if i % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums