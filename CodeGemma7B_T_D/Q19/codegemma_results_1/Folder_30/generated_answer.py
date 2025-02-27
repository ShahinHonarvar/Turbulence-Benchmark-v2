def all_ints_not_div_by_num(nums):
    """
    Returns a list of all integers not divisible by -36 from index 20 to index 35, both exclusive.
    If no such integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for i in range(20, 35):
        if nums[i] % -36 != 0:
            result.append(nums[i])
    return result