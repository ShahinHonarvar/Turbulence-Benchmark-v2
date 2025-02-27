def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(111, len(nums))):
        if 1 < nums[i] and nums[i] < 112:
            is_composite = False
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(nums[i])
    return composite_nums