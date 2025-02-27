def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(30, 31):
        if not is_prime(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums