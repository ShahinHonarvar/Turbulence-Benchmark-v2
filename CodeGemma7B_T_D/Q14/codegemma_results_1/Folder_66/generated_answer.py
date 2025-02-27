def find_second_smallest_num(nums):
    """
    This function takes one argument, a list of distinct numbers, as input and returns
    the second smallest element from index 62 to index 99, both inclusive. If there
    is no such an element, the function should return 'None'.
    """
    if not nums:
        return None
    nums.sort()
    for i in range(62, 100):
        if i < len(nums):
            return nums[i]
    return None