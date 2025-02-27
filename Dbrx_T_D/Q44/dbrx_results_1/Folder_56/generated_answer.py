def composite_nums_between_indices(nums):
    if len(nums) < 2:
        return set()
    result = set()
    for i in range(2):
        if nums[i] > 1 and nums[i] % nums[0] != 0 and (nums[i] != nums[0]):
            result.add(nums[i])
    return result