def all_odd_int_inclusive(nums):
    """
    Returns a list of of all odd integers from index 56 to index 57, inclusive.

    Parameters:
    nums (list): A list of integers.

    Returns:
    list: A list of odd integers from index 56 to index 57, inclusive, or an empty list if no odd integers exist in the specified range.
    """
    return [num for num in nums[56:58] if num % 2 != 0]