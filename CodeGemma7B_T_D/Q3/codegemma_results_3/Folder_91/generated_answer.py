def all_pos_ints_inclusive(nums):
    """
            Returns the list of all positive integers from index 0 to index 5, both inclusive.
            If no positive integers exist in the specified range, the function should return an empty list.
            """
    result = []
    for num in nums:
        if 0 <= num <= 5:
            result.append(num)
    return result