def composite_nums_between_indices(nums):
    """Returns a set of composite numbers in a given list between two indices."""
    composite_nums = set()
    for i in range(50, 201):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or nums[i] % 5 == 0 or (nums[i] % 7 == 0):
            composite_nums.add(nums[i])
    return composite_nums