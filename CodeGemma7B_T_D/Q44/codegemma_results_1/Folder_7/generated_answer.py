def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(527, 539):
        if nums[i] != 1 and nums[i] % 2 != 0:
            for j in range(3, int(nums[i] ** 0.5) + 1, 2):
                if nums[i] % j == 0:
                    composite_set.add(nums[i])
    return composite_set