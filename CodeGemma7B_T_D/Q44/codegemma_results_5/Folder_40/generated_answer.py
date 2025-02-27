def composite_nums_between_indices(nums):
    composites = set()
    for i in range(2, min(2, len(nums)) + 1):
        for j in range(i + 1, len(nums)):
            if nums[i] * nums[j] in nums:
                composites.add(nums[i] * nums[j])
    return composites