def all_pos_ints_inclusive(nums):
    """
            Returns the list of all positive integers from index 15 to index 39, both inclusive.
            If no positive integers exist in the specified range, the function should return an empty list.
            """
    result = []
    for num in nums[15:40]:
        if num > 0:
            result.append(num)
    return result