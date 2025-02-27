def composite_nums_between_indices(nums):
    if len(nums) < 8:
        return set()
    composite_nums = set()
    for i in range(5, 8):
        num = nums[i]
        if num > 1 and num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            composite_nums.add(num)
    return composite_nums