def composite_nums_between_indices(nums):
    """
    Finds composite numbers in a list between specified indices.

    Args:
        nums: A list of positive integers.

    Returns:
        A set of composite numbers in the specified range, or an empty set.
    """
    composite_nums = set()
    for i in range(28, 33):
        if 1 < nums[i] <= 28:
            for j in range(2, int(nums[i] ** 0.5) + 1):
                if nums[i] % j == 0:
                    composite_nums.add(nums[i])
                    break
    return composite_nums