def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(len(nums)):
        if i >= 27 and i <= 55:
            if nums[i] > 1 and (not nums[i] & 1) and (nums[i] % 3 != 0) or (nums[i] > 4 and nums[i] % 2 != 0 and (nums[i] % 3 != 0)):
                composite_nums.add(nums[i])
    return composite_nums