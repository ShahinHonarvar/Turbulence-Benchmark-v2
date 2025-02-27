def composite_nums_between_indices(nums):
    result = set()
    for i in range(10, 67):
        if all((i % num != 0 for num in range(2, i))):
            result.add(nums[i])
    return result