def composite_nums_between_indices(nums):
    composites = []
    for i in range(1, 6):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0:
            composites.append(nums[i])
    return set(composites)