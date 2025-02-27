def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(222, 223):
        if nums[i] > 1 and (not all((num % nums[i] != 0 for num in range(2, nums[i])))):
            composite_nums.add(nums[i])
    return composite_nums