def all_pos_ints_exclusive(nums):
    positive_nums = []
    for i in range(32, min(99, len(nums))):
        if nums[i] > 0:
            positive_nums.append(nums[i])
    return positive_nums