def composite_nums_between_indices(nums):
    composites = set()
    for i in range(29, 52):
        if nums[i] > 1 and (not all((num % nums[i] != 0 for num in range(2, nums[i])))):
            composites.add(nums[i])
    returncomposites