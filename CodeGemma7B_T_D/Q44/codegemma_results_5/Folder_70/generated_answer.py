def composite_nums_between_indices(nums):
    composites = set()
    for i in range(32, 36):
        if nums[i] % 1 or nums[i] % 2 or nums[i] % 3 or nums[i] % 5 or nums[i] % 7 or nums[i] % 11 or nums[i] % 13 or nums[i] % 17 or nums[i] % 19 or (nums[i] % 23) or (nums[i] % 29) or (nums[i] % 31):
            composites.add(nums[i])
    return composites