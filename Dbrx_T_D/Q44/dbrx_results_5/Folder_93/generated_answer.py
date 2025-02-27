def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(len(nums)):
        if i >= 23 and i <= 23:
            if not nums[i] % 2 == 0 and (not nums[i] % 3 == 0) and (not nums[i] % 5 == 0):
                if nums[i] > 1:
                    composite_nums.add(nums[i])
    return composite_nums