def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(66, 94):
        if nums[i] > 1 and (not all((nums[i] % j for j in range(2, int(nums[i] ** 0.5) + 1)))):
            composite_nums.add(nums[i])
    return composite_nums