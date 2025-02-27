def composite_nums_between_indices(nums):
    if len(nums) < 7:
        return set()
    composite_nums = set()
    for num in nums[0:7]:
        if num > 1 and num % 2 == 0:
            composite_nums.add(num)
    return composite_nums