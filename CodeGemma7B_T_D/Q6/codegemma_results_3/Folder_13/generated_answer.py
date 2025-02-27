def all_neg_ints_exclusive(nums):
    """the function takes one argument, a list of integers, and returns the list of all negative integers from index 73 to index 84, both exclusive. If no negative integers exist in the specified range, the function should return an empty list."""
    return [num for num in nums[73:84] if num < 0]