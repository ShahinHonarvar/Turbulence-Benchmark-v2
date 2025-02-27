def find_second_largest_num(nums):
    """
        Finds the second largest number in a list of distinct numbers from index 0 to index 6, both inclusive.

        Args:
        nums: A list of distinct numbers.

        Returns:
        The second largest number from index 0 to index 6, both inclusive. If there is no such element, the function should return 'None'.
        """
    if not nums or len(nums) < 3:
        return None
    first_largest = float('-inf')
    second_largest = float('-inf')
    for num in nums:
        if num > first_largest:
            first_largest, second_largest = (num, first_largest)
        elif num > second_largest:
            second_largest = num
    if second_largest != float('-inf'):
        return second_largest
    else:
        return None