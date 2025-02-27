def composite_nums_between_indices(nums):
    return set(filter(lambda x: 1 < x < nums[62] and x > nums[63] and (x % nums[61] != 0) and (x % nums[64] != 0), nums[62:63 + 1]))