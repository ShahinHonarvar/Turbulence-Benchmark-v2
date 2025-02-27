def all_pos_ints_exclusive(nums):
    """
    This function takes one argument, a list of integers, and returns the list of all positive integers from index 100 to index 200, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.
    """
    pos_ints = []
    for num in nums:
        if num > 0 and 100 < nums.index(num) < 200:
            pos_ints.append(num)
    return pos_ints