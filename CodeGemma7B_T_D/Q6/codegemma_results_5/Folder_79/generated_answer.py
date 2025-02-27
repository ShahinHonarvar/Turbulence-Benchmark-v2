def all_neg_ints_exclusive(nums):
    """
            Returns a list of all negative integers from index 3 to index 8, both exclusive.
            """
    return [num for num in nums[3:8] if num < 0]