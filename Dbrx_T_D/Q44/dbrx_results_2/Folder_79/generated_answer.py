def composite_nums_between_indices(nums):
    if len(nums) < 7:
        return set()
    composite_nums = set()
    for i in range(6, 8):
        if i < len(nums) and nums[i] > 1 and (not (nums[i] % 2 == 0 and nums[i] > 2)):
            is_composite = False
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(nums[i])
    return composite_nums