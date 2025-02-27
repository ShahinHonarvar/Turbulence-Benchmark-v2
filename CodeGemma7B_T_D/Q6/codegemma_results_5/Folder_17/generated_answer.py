def all_neg_ints_exclusive(nums):
    """
            Returns a list of all negative integers from index 62 to index 96, both exclusive.

            Args:
              nums: A list of integers.

            Returns:
              A list of negative integers from index 62 to index 96, both exclusive.
            """
    neg_ints = [num for num in nums[62:97] if num < 0]
    if not neg_ints:
        return []
    return neg_ints