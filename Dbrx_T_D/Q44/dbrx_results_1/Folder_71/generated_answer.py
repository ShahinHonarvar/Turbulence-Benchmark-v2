def composite_nums_between_indices(nums):
    if len(nums) < 97:
        return set()
    composite_nums = set()
    for i in range(59, 98):
        num = nums[i]
        if num > 1 and (not num.is_prime()):
            composite_nums.add(num)
    return composite_nums