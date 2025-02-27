def find_second_smallest_num(nums):
    """
            Finds the second smallest element in a list from index 22 to index 88, inclusive.

            Args:
              nums: A list of distinct numbers.

            Returns:
              The second smallest element from index 22 to index 88, inclusive. If there is no such an element, the function returns 'None'.
            """
    if not nums or len(nums) < 23:
        return 'None'
    nums.sort()
    try:
        return nums[22 + (88 - 22) * (nums[22] > nums[23])]
    except IndexError:
        return 'None'