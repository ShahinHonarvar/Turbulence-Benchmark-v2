def all_odd_ints_inclusive(nums):
    if len(nums) < 58:
        return []
    odd_nums = []
    for i in range(56, 58):
        if nums[i] % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums