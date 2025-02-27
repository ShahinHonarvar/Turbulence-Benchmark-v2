def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(90, 201):
        if nums[i] > 1 and all((num % nums[i] != 0 for num in range(2, int(nums[i] ** 0.5 + 1)))):
            composite_nums.add(nums[i])
    return composite_nums