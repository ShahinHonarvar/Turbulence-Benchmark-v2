def all_neg_ints_exclusive(nums):
    """
    This function takes one argument, a list of integers, and returns the list of all negative integers from index 4 to index 5, both exclusive. If no negative integers exist in the specified range, the function should return an empty list.
    """
    target_list = []
    for num in nums[4:5]:
        if num < 0:
            target_list.append(num)
    return target_list