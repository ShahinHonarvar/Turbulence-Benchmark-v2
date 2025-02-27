def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(len(nums)):
        if i >= 0 and i <= 7 and (not is_prime(nums[i])):
            composite_nums.add(nums[i])
    return composite_nums