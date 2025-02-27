def all_pos_ints_inclusive(nums):
    for i in range(4, len(nums)):
        if nums[i] > 0:
            return nums[i:i + 5]
    return []