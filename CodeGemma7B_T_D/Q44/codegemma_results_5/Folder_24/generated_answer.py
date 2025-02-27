def composite_nums_between_indices(nums):
    composites = set()
    for i in range(34, 56):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or any((nums[i] % j == 0 for j in range(5, int(nums[i] ** 0.5) + 1, 6))):
            composites.add(nums[i])
    return composites