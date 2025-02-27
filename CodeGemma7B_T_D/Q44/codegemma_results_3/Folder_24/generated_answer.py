def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(34, 56):
        if nums[i % len(nums)] % 2 == 0 or nums[i % len(nums)] in range(3, 7):
            composite_nums.add(nums[i % len(nums)])
    return composite_nums