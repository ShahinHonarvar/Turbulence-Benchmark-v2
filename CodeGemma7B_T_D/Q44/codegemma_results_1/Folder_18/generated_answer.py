def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(25, 88):
        if nums[i] % 2 != 0 and nums[i] % 3 != 0:
            for j in range(5, int(nums[i] ** 0.5) + 1, 6):
                if nums[i] % j == 0 or nums[i] % (j + 2) == 0:
                    composite_nums.add(nums[i])
    return composite_nums