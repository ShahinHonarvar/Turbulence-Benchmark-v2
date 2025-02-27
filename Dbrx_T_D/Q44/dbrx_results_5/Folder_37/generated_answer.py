def composite_nums_between_indices(nums):
    composite_nums = set()
    if len(nums) < 6:
        return composite_nums
    for i in range(0, 6):
        if i >= len(nums):
            break
        if nums[i] > 1 and (not (nums[i] == 2 or nums[i] == 3 or nums[i] == 5)) and (nums[i] % 2 != 0) and (nums[i] % 3 != 0) and (nums[i] % 5 != 0):
            composite_nums.add(nums[i])
    return composite_nums