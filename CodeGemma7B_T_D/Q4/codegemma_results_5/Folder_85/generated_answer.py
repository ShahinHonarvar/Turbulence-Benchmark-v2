def all_pos_ints_exclusive(nums: list[int]) -> list[int]:
    """Return the list of all positive integers from index 4 to index 5, both exclusive. If no positive integers exist in the specified range, the function should return an empty list."""
    result = []
    for num in nums[4:5]:
        if num > 0:
            result.append(num)
    return result