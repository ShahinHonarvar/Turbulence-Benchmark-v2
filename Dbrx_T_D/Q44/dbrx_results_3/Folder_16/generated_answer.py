def composite_nums_between_indices(nums):
    if len(nums) < 81:
        return set()
    composite_nums = set()
    for i in range(40, 81):
        if i >= len(nums):
            break
        if nums[i] > 1 and (nums[i] % 2 == 0 or nums[i] % 3 == 0):
            composite_nums.add(nums[i])
    return composite_nums