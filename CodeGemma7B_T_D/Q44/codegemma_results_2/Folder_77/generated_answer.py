def composite_nums_between_indices(nums):
    """
    This function takes a list of positive integers as input and returns the set of all composite numbers in the given list that are between index 667 to index 774, both inclusive. If no composite number exists in the specified range, the function returns an empty set.
    """
    composites = set()
    for i in range(667, 775):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0:
            composites.add(nums[i])
    return composites