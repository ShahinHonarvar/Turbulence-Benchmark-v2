def composite_nums_between_indices(nums):
    if len(nums) < 100:
        return set()
    composite_nums = set()
    for i in range(10, 101):
        if i < len(nums) and nums[i] > 1:
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    composite_nums.add(nums[i])
                    break
    return composite_nums