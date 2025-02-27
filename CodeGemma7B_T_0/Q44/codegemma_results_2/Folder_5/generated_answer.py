def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(1, 6):
        if i in nums and (not is_prime(i)):
            composite_nums.add(i)
    return composite_nums