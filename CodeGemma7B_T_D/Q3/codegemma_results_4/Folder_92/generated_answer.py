def all_pos_ints_inclusive(nums):
    """
        Returns the list of all positive integers from index 0 to index 1, both inclusive.

        Args:
            nums: A list of integers.

        Returns:
            A list of positive integers from index 0 to index 1, both inclusive. If no positive integers exist in the specified range, an empty list is returned.
        """
    pos_nums = []
    for num in nums:
        if num > 0:
            pos_nums.append(num)
    if not pos_nums:
        return []
    return pos_nums[:2] + nums[1:3] + nums[-2:]