import math

def all_neg_ints_inclusive(nums):
    """
    Returns a list of all negative integers from index 10 to index 100, both inclusive.
    If no negative integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[10:101] if num <= 0]