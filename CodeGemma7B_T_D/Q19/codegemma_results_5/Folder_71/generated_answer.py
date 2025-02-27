def all_ints_not_div_by_num(nums):
    """
    This function takes a list of integers and returns the list of all integers not divisible by -77 from index 21 to index 51, both exclusive. If no such integers exist in the specified range, the function should return an empty list.
    """
    valid_ints = []
    for i in range(21, 51):
        if nums[i] % -77 != 0:
            valid_ints.append(nums[i])
    return valid_ints