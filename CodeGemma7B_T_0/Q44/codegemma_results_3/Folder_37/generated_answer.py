def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(len(nums)):
        if i in range(0, 6):
            if not (nums[i] == 2 or nums[i] == 3):
                if nums[i] % 2 == 0 or nums[i] % 3 == 0:
                    composite_set.add(nums[i])
    return composite_set