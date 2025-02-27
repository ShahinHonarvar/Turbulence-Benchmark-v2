def composite_nums_between_indices(nums):
    composites = set()
    for i in range(29, 52):
        if nums[i] > 1 and all((num % nums[i] != 0 for num in range(2, int(nums[i] ** 0.5) + 1))):
            composites.add(nums[i])
    return composites