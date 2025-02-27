def all_pos_ints_inclusive(nums):
    positive_ints = []
    for i in range(82, 87):
        if i < len(nums) and nums[i] > 0:
            positive_ints.append(nums[i])
    return positive_ints