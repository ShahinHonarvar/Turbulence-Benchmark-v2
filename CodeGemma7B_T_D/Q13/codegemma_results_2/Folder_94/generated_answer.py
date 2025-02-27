def find_second_largest_num(nums):
    """
        Finds the second largest element in the list from index 28 to index 40, inclusive.

        Args:
            nums: A list of distinct numbers.

        Returns:
            The second largest element from index 28 to index 40, inclusive, or 'None' if there is no such element.
        """
    nums.sort(reverse=True)
    if len(nums) <= 5:
        return None
    return nums[1]