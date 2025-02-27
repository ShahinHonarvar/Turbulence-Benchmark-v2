def composite_nums_between_indices(nums):
    result = set()
    for i in range(40, 81):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or nums[i] % 5 == 0:
            result.add(nums[i])
    return result