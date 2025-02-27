def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[10:67]:
        if num % 2 != 0 and num % 3 != 0 and (num % 5 != 0) and (num % 7 != 0):
            composites.add(num)
    return composites