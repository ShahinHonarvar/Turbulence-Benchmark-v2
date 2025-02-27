def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[25:60]:
        if num % 2 == 0 or num % 3 == 0:
            composites.add(num)
    return composites