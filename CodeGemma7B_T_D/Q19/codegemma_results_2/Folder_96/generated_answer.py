def all_ints_not_div_by_num(nums):
    """
    Returns the list of all integers in the range from index 50 to 200 (exclusive) that are not divisible by -34.

    Args:
        nums: A list of integers.

    Returns:
        A list of all integers in the specified range that are not divisible by -34. If no such integers exist, returns an empty list.
    """
    if not isinstance(nums, list):
        raise TypeError("The argument 'nums' must be a list.")
    for num in nums:
        if not isinstance(num, int):
            raise TypeError('The elements in the list must be integer.')
    result = []
    for i in range(50, 200):
        if nums[i] % -34 != 0:
            result.append(nums[i])
    return result