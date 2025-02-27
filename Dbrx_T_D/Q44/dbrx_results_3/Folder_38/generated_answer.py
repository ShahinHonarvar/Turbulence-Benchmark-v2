def composite_nums_between_indices(nums):
    range_composites = set()
    for i in range(len(nums)):
        if i >= 29 and i <= 93 and (nums[i] > 1) and (nums[i] % 2 == 0 or nums[i] % 3 == 0):
            range_composites.add(nums[i])
    return range_composites