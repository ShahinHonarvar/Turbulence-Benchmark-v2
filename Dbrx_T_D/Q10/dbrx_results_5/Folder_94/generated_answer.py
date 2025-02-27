def all_odd_ints_exclusive(nums):
    odd_ints = []
    for i in range(28, 53):
        if i < len(nums) and nums[i] % 2 != 0:
            odd_ints.append(nums[i])
    return odd_ints