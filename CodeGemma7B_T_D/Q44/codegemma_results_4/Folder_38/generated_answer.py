def composite_nums_between_indices(nums):
    composites = set()
    if len(nums) >= 93 and nums[29] > 1 and (nums[93] > 1):
        for i in range(29, 94):
            if nums[i] > 1 and any((num * num <= nums[i] for num in range(2, int(nums[i] ** 0.5) + 1))):
                composites.add(nums[i])
    return composites