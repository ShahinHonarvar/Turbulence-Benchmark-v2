def find_second_smallest_num(nums):
    """
    This function takes one argument, a list of distinct numbers.
    It returns the second smallest element from index 33 to index 36, both inclusive.
    If there is no such an element, the function should return 'None'.
    """
    nums_slice = nums[33:37]
    if not nums_slice:
        return None
    return min(nums_slice)