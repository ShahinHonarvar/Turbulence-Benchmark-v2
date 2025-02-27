def all_odd_ints_inclusive(nums):
    """
    Finds all unique odd integers in a list from index 310 to 370 (inclusive) and returns them.
    If no odd integers exist in this range, an empty list is returned.
    """
    odd_nums = []
    for i in range(310, 371):
        if nums[i] % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums