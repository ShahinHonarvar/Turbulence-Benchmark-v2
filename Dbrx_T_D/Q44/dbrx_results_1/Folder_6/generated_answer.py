def composite_nums_between_indices(nums):
    if len(nums) < 69:
        return set()
    composite_nums = set()
    for i in range(13, 69):
        if i >= len(nums):
            break
        num = nums[i]
        if num > 1 and (not (num == 2 or (num % 2 == 0 and num != 0))):
            composite_nums.add(num)
    return composite_nums