def all_odd_ints_exclusive(nums):
    if len(nums) < 88:
        return []
    odd_ints = []
    for i in range(81, 86):
        num = nums[i]
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints