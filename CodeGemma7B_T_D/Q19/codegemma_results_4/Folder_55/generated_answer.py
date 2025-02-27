def all_ints_not_div_by_num(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return [num for num in nums[0:10] if num % 10 != 0]