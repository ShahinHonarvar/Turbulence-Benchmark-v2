def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(4, len(nums)):
        if not is_prime(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums