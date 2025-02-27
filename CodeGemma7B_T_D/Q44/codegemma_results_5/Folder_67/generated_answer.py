def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(56, 83):
        if nums[i] != 1 and (not all((num <= 1 or num == nums[i] for num in range(2, int(nums[i] ** 0.5) + 1)))):
            composite_nums.add(nums[i])
    return composite_nums