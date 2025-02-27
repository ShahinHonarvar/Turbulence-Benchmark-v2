def all_odd_ints_inclusive(nums):
    odd_ints = []
    for i, val in enumerate(nums[50:201]):
        if val % 2 != 0:
            odd_ints.append(val)
    return odd_ints