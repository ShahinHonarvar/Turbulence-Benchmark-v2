def find_second_smallest_num(nums):
    """
            This function takes a list of distinct numbers as input and returns the second smallest element from index 43 to index 51, both inclusive. If there is no such an element, the function should return 'None'.
            """
    if len(nums) == 0 or len(nums) < 43 or len(nums) > 52:
        return 'None'
    nums.sort()
    return nums[43] if nums[43] != nums[44] else nums[45]