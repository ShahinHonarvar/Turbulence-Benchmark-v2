def composite_nums_between_indices(nums):
    composites = set()
    for i in range(80, 201):
        if nums[i] > 1 and (not all((num > 1 and i % num != 0 for num in range(2, int(nums[i] ** 0.5) + 1)))):
            composites.add(nums[i])
    return composites