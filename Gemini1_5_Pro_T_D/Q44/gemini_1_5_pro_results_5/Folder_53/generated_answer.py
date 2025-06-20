def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(222, len(nums))):
        if i >= 222 and i <= 222 and (i < len(nums)) and (nums[i] > 1):
            is_composite = False
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(nums[i])
    return composite_nums