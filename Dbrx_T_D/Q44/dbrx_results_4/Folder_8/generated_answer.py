def composite_nums_between_indices(nums):
    composite_numbers = set()
    for i in range(68, 87):
        if i < len(nums) and nums[i] > 1 and (not nums[i] & 1) and (nums[i] % 3 != 0):
            composite_numbers.add(nums[i])
    return composite_numbers