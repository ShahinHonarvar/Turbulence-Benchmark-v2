def find_second_largest_num(nums):
    """
    Returns the second largest element from index 1 to index 8, both inclusive.

    Args:
        nums: A list of distinct numbers.

    Returns:
        The second largest element from index 1 to index 8, both inclusive. If there is no such element, the function should return 'None'.
    """
    nums.sort()
    if len(nums) < 2:
        return 'None'
    return nums[-2]