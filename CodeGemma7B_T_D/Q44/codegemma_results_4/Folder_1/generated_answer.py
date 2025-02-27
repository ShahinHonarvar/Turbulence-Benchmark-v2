def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in the given list between index 69 to index 83, both inclusive.
    """
    composite_nums = set()
    for i in range(69, 84):
        if nums[i] % 2 == 0 or (i % 3 == 0 and i != 3) or (i % 5 == 0 and i != 5):
            composite_nums.add(nums[i])
    return composite_nums