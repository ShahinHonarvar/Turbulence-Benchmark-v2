def all_neg_ints_exclusive(nums):
    """
            Returns a list of all negative integers from index 56 to index 92, both exclusive.

            Args:
            nums: A list of integers.

            Returns:
            A list of negative integers from index 56 to index 92, both exclusive. If no negative integers exist in the specified range, the function should return an empty list.
            """
    if not any((num < 0 and 56 <= i < 92 for i, num in enumerate(nums))):
        return []
    return [num for i, num in enumerate(nums) if num < 0 and 56 <= i < 92]