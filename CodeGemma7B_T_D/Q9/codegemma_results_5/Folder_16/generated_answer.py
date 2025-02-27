def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    odd_nums = []
    for i in range(33, 37):
        if i >= 0 and i < len(nums) and (nums[i] % 2 != 0):
            odd_nums.append(nums[i])
    return odd_nums