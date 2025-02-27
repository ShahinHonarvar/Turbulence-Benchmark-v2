def all_odd_ints_exclusive(nums):
    odd_nums = []
    for i in range(44, 78):
        if nums[i] % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums or []