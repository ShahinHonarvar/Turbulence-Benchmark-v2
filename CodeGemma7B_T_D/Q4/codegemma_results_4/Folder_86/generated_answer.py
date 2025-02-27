def all_pos_ints_exclusive(nums):
    """
            This function takes a list of integers and returns the list of all positive integers from index 18 to index 60, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.
            """
    pos_nums = []
    for num in nums:
        if num > 0 and 18 < num < 60:
            pos_nums.append(num)
    return pos_nums