def find_second_smallest_num(nums):
    """
    Finds the second smallest element in a list of distinct numbers from index 43 to index 86, inclusive.

    Args:
        nums: A list of distinct numbers.

    Returns:
        The second smallest element from index 43 to index 86, inclusive. If there is no such element, the function returns 'None'.
    """
    nums.sort()
    if len(nums) < 87 or nums[86] == nums[42]:
        return None
    return nums[44]