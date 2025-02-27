def composite_nums_between_indices(nums):
    result = set()
    for i in range(686, 988):
        if nums[i] % 2 or nums[i] % 3 or nums[i] % 5 or (nums[i] % 7 != 0):
            if nums[i] > 1:
                result.add(nums[i])
    return result