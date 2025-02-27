def all_neg_ints_inclusive(nums):
    """
    This function takes one argument, a list of integers, and returns the list of all
    negative integers from index 75 to index 85, both inclusive. If no negative
    integers exist in the specified range, the function should return an empty list.
    """
    neg_nums = []
    for i in range(75, 86):
        if nums[i] < 0:
            neg_nums.append(nums[i])
    return neg_nums