def composite_nums_between_indices(nums):
    """:param nums: A list of positive integers."""
    ':return: The set of composite numbers in the given list between indices 22 to 88, both inclusive. If no composite number exists in the specified range, the function should return an empty set.'
    composite_nums = set()
    for i in range(22, 89):
        if nums[i] not in (2, 3) and (not all((nums[i] % d != 0 for d in range(2, int(nums[i] ** 0.5) + 1)))):
            composite_nums.add(nums[i])
    return composite_nums if composite_nums else set()