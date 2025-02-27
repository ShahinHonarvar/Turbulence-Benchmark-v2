def all_odd_ints_inclusive(nums):
    odd_ints = []
    for i in range(75, 86):
        if nums[i] % 2 != 0:
            odd_ints.append(nums[i])
    return odd_ints