def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(nums[6], nums[6] + 1):
        if not is_prime(i):
            composite_nums.add(i)
    return composite_nums