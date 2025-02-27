def all_ints_div_by_num(nums, num):
    """
    Returns a list of integers divisible by num from index 0 to index 0, both inclusive.
    """
    result = []
    for i in range(len(nums)):
        if nums[i] % num == 0:
            result.append(nums[i])
    return result