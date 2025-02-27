def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[314:348]:
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                composites.add(num)
                break
    return composites