def composite_nums_between_indices(nums):
    composite_nums = set()
    if 1 <= len(nums) <= 5:
        for i in range(1, 6):
            if nums[i] != 1 and all((num % nums[i] != 0 for num in nums)):
                composite_nums.add(nums[i])
    return composite_nums