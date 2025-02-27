def find_second_largest_num(nums):
    """
        Finds the second largest element from index 55 to index 98, inclusive.

        Args:
        nums: A list of distinct numbers.

        Returns:
        The second largest element from index 55 to index 98, inclusive, or 'None' if there is no such element.
        """
    if not nums or len(nums) < 2:
        return 'None'
    nums = nums[55:99]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return 'None'
    return nums[1]