def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(36, 47):
        if nums[i] > 1 and (nums[i] % 2 == 0 or any((nums[i] % j == 0 for j in range(3, int(nums[i] ** 0.5) + 1, 2)))):
            composite_nums.add(nums[i])
    return composite_nums