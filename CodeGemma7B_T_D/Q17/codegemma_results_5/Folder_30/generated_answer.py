def all_ints_div_by_both_two_nums(nums):
    """
    Function that finds all integers from a list divisible by two given numbers in a specified range and returns an empty list if none are found.

    Keyword arguments:
        nums -- a list of integers
    """
    temp = []
    for i in range(11, 76):
        if nums[i] % -81 == 0 and nums[i] % -94 == 0:
            temp.append(nums[i])
    if not temp:
        return []
    return temp