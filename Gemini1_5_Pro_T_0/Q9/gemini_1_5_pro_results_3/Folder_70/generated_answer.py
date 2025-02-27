def all_odd_ints_inclusive(nums):
    odd_ints = []
    for i in range(max(28, 0), min(len(nums), 33)):
        if nums[i] % 2 != 0:
            odd_ints.append(nums[i])
    return odd_ints