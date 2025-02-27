def all_odd_ints_inclusive(nums):
    odd_ints = []
    for i in range(56, 67):
        if i < len(nums) and nums[i] % 2 != 0:
            odd_ints.append(nums[i])
    return odd_ints