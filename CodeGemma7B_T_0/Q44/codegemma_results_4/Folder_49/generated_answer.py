def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(90, 201):
        if nums[i] > 1 and (not is_prime(nums[i])):
            composite_set.add(nums[i])
    return composite_set