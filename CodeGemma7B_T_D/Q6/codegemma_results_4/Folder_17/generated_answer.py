def all_neg_ints_exclusive(nums):
    """
        This function takes a list of integers as an argument and returns a list of all negative integers from index 62 to index 96, both exclusive.
        If no negative integers exist in the specified range, the function should return an empty list.
        """
    neg_ints = []
    for num in nums[62:96]:
        if num < 0:
            neg_ints.append(num)
    return neg_ints