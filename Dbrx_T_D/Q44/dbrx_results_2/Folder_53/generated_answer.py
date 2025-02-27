def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(222, 222 + 1):
        if i < len(nums) and i >= 0 and (nums[i] > 1):
            is_composite = False
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(nums[i])
    return composite_nums