def all_odd_ints_exclusive(nums):
    """ Returns a list of all odd integers in the specified range (inclusive of the starting index but exclusive of the ending index). """
    odd_nums = []
    for i in range(80, 200):
        if nums[i] % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums