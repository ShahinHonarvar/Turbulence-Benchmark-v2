def find_second_smallest_num(nums):
    """
            Finds the second smallest number from index 3 to index 5, both inclusive.

            Args:
                nums: A list of distinct numbers.

            Returns:
                The second smallest element from index 3 to index 5, both inclusive. If there is no such an element, the function should return 'None'.
            """
    nums.sort()
    if len(nums) < 5:
        return 'None'
    return nums[3:6][1]