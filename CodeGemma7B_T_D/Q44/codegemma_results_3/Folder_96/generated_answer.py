def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in the given list that are between index 60 to index 200, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    """
    composite_nums = set()
    for i in range(60, 201):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0:
            composite_nums.add(nums[i])
    return composite_nums