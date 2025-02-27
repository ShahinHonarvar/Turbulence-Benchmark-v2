def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[43:52]:
        for factor in range(2, num):
            if num % factor == 0:
                composites.add(num)
                break
    return composites