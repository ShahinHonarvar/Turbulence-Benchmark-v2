def composite_nums_between_indices(nums):
    composites = set()
    for i in range(43, 52):
        if i >= len(nums) or nums[i] % 2 == 0 or any((i % d == 0 for d in range(3, int(i ** 0.5) + 1, 2))):
            composites.add(nums[i])
    return composites