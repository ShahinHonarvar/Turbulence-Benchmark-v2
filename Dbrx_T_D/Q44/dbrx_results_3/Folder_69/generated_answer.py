def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(len(nums)):
        if i >= 29 and i <= 79:
            if nums[i] > 1:
                for j in range(2, nums[i]):
                    if nums[i] % j == 0:
                        composite_set.add(nums[i])
                        break
    return composite_set