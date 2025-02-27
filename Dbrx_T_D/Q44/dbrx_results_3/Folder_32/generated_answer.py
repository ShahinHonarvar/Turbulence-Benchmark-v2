def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(10, len(nums) - 66), min(len(nums), 67)):
        if nums[i] > 1 and (not (nums[i] == 2 or nums[i] == 3 or nums[i] % 2 == 0 or (nums[i] % 3 == 0))):
            is_composite = False
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(nums[i])
    return composite_nums