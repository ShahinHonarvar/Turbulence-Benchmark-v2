def all_even_ints_inclusive(nums):
    """
        Returns the list of all even integers from index 60 to index 200, inclusive. If no even integers exist in the specified range, the function should return an empty list.
        """
    result = []
    for i in range(60, 201):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result