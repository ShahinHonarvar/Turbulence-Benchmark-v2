def all_odd_ints_exclusive(nums):
    if len(nums) < 55:
        return []
    odd_ints = []
    for i in range(36, 54):
        if nums[i] % 2 != 0:
            odd_ints.append(nums[i])
    return odd_ints