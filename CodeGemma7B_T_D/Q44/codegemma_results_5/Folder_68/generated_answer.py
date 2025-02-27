def composite_nums_between_indices(nums):
    composites = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] * nums[j] in nums[i:j + 1]:
                composites.add(nums[i] * nums[j])
    return composites if composites else set()